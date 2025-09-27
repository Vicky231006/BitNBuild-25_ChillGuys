from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any, Optional
import pandas as pd
import pdfplumber
import io
import re
from datetime import datetime, timedelta
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor
import uuid
from dataclasses import dataclass, asdict
from enum import Enum
import threading
import time
import logging
from pathlib import Path
import os

# Simple logging setup for Railway
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Financial Data Processing Hub - Railway Ready", 
    version="2.2.0",
    description="Railway-optimized financial data processing API"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Railway-optimized storage (memory only)
PROCESSED_DATA_STORE = {}
PROCESSING_STATUS = {}
CATEGORY_CACHE = {}

# File validation constants
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB for Railway free tier
MAX_FILES = 3
ALLOWED_EXTENSIONS = {'.csv', '.pdf'}

class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"
    EMI = "emi"
    CREDIT_CARD = "credit_card"
    INVESTMENT = "investment"

@dataclass
class ProcessedTransaction:
    id: str
    date: str
    description: str
    amount: float
    category: str
    type: TransactionType
    subcategory: Optional[str] = None
    is_recurring: bool = False
    source_file: str = ""
    confidence_score: float = 1.0
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'description': self.description,
            'amount': self.amount,
            'category': self.category,
            'type': self.type.value,
            'subcategory': self.subcategory,
            'is_recurring': self.is_recurring,
            'source_file': self.source_file,
            'confidence_score': self.confidence_score
        }

@dataclass
class ProcessedFinancialData:
    session_id: str
    summary: Dict[str, Any]
    transactions: List[ProcessedTransaction]
    income_analysis: Dict[str, Any]
    expense_analysis: Dict[str, Any]
    credit_behavior: Dict[str, Any]
    tax_relevant_data: Dict[str, Any]
    processing_errors: List[str]
    processing_warnings: List[str]
    created_at: str
    
    def to_json(self):
        return {
            'session_id': self.session_id,
            'summary': self.summary,
            'transactions': [t.to_dict() for t in self.transactions],
            'income_analysis': self.income_analysis,
            'expense_analysis': self.expense_analysis,
            'credit_behavior': self.credit_behavior,
            'tax_relevant_data': self.tax_relevant_data,
            'processing_errors': self.processing_errors,
            'processing_warnings': self.processing_warnings,
            'created_at': self.created_at
        }

# Enhanced categorization with confidence scores
ENHANCED_CATEGORY_MAPPING = {
    # High confidence patterns
    r'salary|wage|income|pay(?!ment)|payroll': ('Income', 'Salary', 0.95),
    r'bonus|incentive|commission': ('Income', 'Bonus', 0.90),
    r'dividend|interest(?!.*pay)|fd|fixed.deposit': ('Income', 'Investment_Returns', 0.90),
    
    # EMI patterns (critical for CIBIL)
    r'emi|equated.*monthly|loan.*emi|home.*loan|car.*loan|personal.*loan': ('EMI', 'Loan_EMI', 0.95),
    r'mortgage|housing.*loan|property.*loan': ('EMI', 'Home_Loan', 0.95),
    r'education.*loan|student.*loan': ('EMI', 'Education_Loan', 0.90),
    
    # Credit card patterns
    r'credit.*card|cc.*payment|card.*payment': ('Credit_Card', 'CC_Payment', 0.90),
    r'credit.*card.*bill|cc.*bill': ('Credit_Card', 'CC_Bill', 0.90),
    
    # Tax-saving investments
    r'mutual.*fund|sip|systematic|elss|tax.*saver': ('Investment', 'Tax_Saving', 0.85),
    r'provident.*fund|pf|ppf|epf': ('Investment', 'PF_PPF', 0.95),
    r'insurance|lic|health.*insurance|term.*insurance': ('Insurance', 'Tax_Deductible', 0.85),
    
    # Common expenses
    r'rent(?!al)|rental.*paid': ('Housing', 'Rent', 0.90),
    r'electricity|power|water|gas|internet|mobile|phone': ('Utilities', 'Bills', 0.85),
    r'grocery|supermarket|vegetables|provisions': ('Food', 'Groceries', 0.85),
    r'restaurant|zomato|swiggy|food.*delivery|uber.*eats': ('Food', 'Dining', 0.90),
    r'uber|ola|taxi|metro|bus|transport|fuel|petrol|diesel': ('Transportation', 'Travel', 0.85),
    r'medical|doctor|hospital|pharmacy|medicine': ('Healthcare', 'Medical', 0.85),
}

def validate_uploaded_file(file: UploadFile) -> bool:
    """Railway-optimized file validation"""
    # Check file size
    file.file.seek(0, 2)  # Go to end
    file_size = file.file.tell()
    file.file.seek(0)  # Reset
    
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413, 
            detail=f"File {file.filename} too large ({file_size/1024/1024:.1f}MB). Maximum {MAX_FILE_SIZE/1024/1024}MB allowed."
        )
    
    # Check file extension
    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400, 
            detail=f"File type {file_ext} not allowed. Supported: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    return True

def enhanced_categorize_transaction(description: str, amount: float) -> tuple:
    """Enhanced categorization with confidence scores"""
    cache_key = description.lower()[:30]
    
    if cache_key in CATEGORY_CACHE:
        return CATEGORY_CACHE[cache_key]
    
    description_lower = description.lower()
    best_match = None
    best_confidence = 0.0
    
    for pattern, (category, subcategory, confidence) in ENHANCED_CATEGORY_MAPPING.items():
        if re.search(pattern, description_lower):
            if confidence > best_confidence:
                best_match = (category, subcategory, confidence)
                best_confidence = confidence
    
    if best_match:
        category, subcategory, confidence = best_match
        # Determine transaction type
        if category == 'Income':
            trans_type = TransactionType.INCOME
        elif category in ['EMI', 'Credit_Card']:
            trans_type = TransactionType.EMI if category == 'EMI' else TransactionType.CREDIT_CARD
        elif category == 'Investment':
            trans_type = TransactionType.INVESTMENT
        else:
            trans_type = TransactionType.EXPENSE
        
        result = (category, subcategory, trans_type, confidence)
    else:
        # Default categorization
        if amount > 0:
            result = ('Other_Income', 'Miscellaneous', TransactionType.INCOME, 0.3)
        else:
            result = ('Other_Expense', 'Miscellaneous', TransactionType.EXPENSE, 0.3)
    
    CATEGORY_CACHE[cache_key] = result
    return result

def parse_date_robust(date_str: str) -> str:
    """Robust date parsing"""
    if not date_str or str(date_str).lower() in ['nan', 'none', '']:
        return datetime.now().strftime('%Y-%m-%d')
    
    date_str = str(date_str).strip()
    
    # Common date formats
    formats = [
        '%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%d-%m-%Y', '%m-%d-%Y',
        '%d/%m/%y', '%m/%d/%y', '%d-%m-%y', '%m-%d-%y',
        '%d %b %Y', '%d %B %Y', '%b %d, %Y', '%B %d, %Y',
    ]
    
    for fmt in formats:
        try:
            parsed_date = datetime.strptime(date_str[:len(fmt)], fmt)
            return parsed_date.strftime('%Y-%m-%d')
        except:
            continue
    
    logger.warning(f"Could not parse date: {date_str}")
    return datetime.now().strftime('%Y-%m-%d')

def clean_amount_robust(amount_str: str) -> float:
    """Robust amount cleaning"""
    if not amount_str or str(amount_str).lower() in ['nan', 'none', '']:
        return 0.0
    
    amount_str = str(amount_str)
    
    # Check for negative indicators
    is_negative = any(indicator in amount_str for indicator in ['(', ')', '-', 'DR', 'Debit'])
    
    # Clean the string
    cleaned = re.sub(r'[₹$£€,\s()DRCrdebitcredit]', '', amount_str, flags=re.IGNORECASE)
    
    try:
        amount = float(cleaned)
        return -amount if is_negative else amount
    except ValueError:
        logger.warning(f"Could not parse amount: {amount_str}")
        return 0.0

def process_csv_optimized(file_content: bytes, filename: str) -> List[ProcessedTransaction]:
    """Railway-optimized CSV processing"""
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
    df = None
    
    for encoding in encodings:
        try:
            df = pd.read_csv(
                io.BytesIO(file_content),
                encoding=encoding,
                dtype=str,
                parse_dates=False,
                on_bad_lines='skip',
                low_memory=False
            )
            logger.info(f"Successfully decoded {filename} with {encoding}")
            break
        except Exception as e:
            logger.debug(f"Failed {encoding} for {filename}: {e}")
            continue
    
    if df is None:
        raise ValueError(f"Could not decode {filename}")
    
    # Normalize column names
    df.columns = df.columns.str.lower().str.strip()
    
    # Column mapping
    column_mappings = {
        'transaction date': 'date', 'trans date': 'date', 'txn date': 'date',
        'value date': 'date', 'posting date': 'date', 'transaction_date': 'date',
        'description': 'description', 'narration': 'description', 'particulars': 'description',
        'transaction details': 'description', 'remarks': 'description', 'details': 'description',
        'amount': 'amount', 'transaction amount': 'amount', 'txn amount': 'amount',
        'debit': 'debit', 'credit': 'credit', 'withdrawal': 'debit', 'deposit': 'credit',
    }
    
    df = df.rename(columns=column_mappings)
    
    transactions = []
    
    for idx, row in df.iterrows():
        try:
            date_str = str(row.get('date', '')).strip()
            if not date_str or date_str.lower() in ['nan', 'none']:
                continue
            
            date = parse_date_robust(date_str)
            description = str(row.get('description', f'Transaction {idx}')).strip()
            
            # Calculate amount
            amount = 0.0
            if 'amount' in df.columns and pd.notna(row.get('amount')):
                amount = clean_amount_robust(str(row['amount']))
            elif 'debit' in df.columns or 'credit' in df.columns:
                debit = clean_amount_robust(str(row.get('debit', '0')))
                credit = clean_amount_robust(str(row.get('credit', '0')))
                amount = credit - abs(debit)
            
            if amount == 0:
                continue
            
            # Categorization
            category, subcategory, trans_type, confidence = enhanced_categorize_transaction(description, amount)
            
            transaction = ProcessedTransaction(
                id=str(uuid.uuid4()),
                date=date,
                description=description,
                amount=amount,
                category=category,
                type=trans_type,
                subcategory=subcategory,
                source_file=filename,
                confidence_score=confidence
            )
            
            transactions.append(transaction)
            
        except Exception as e:
            logger.warning(f"Skipping row {idx}: {e}")
            continue
    
    return transactions

def process_pdf_optimized(file_content: bytes, filename: str) -> List[ProcessedTransaction]:
    """Railway-optimized PDF processing"""
    transactions = []
    
    try:
        with pdfplumber.open(io.BytesIO(file_content)) as pdf:
            for page_num, page in enumerate(pdf.pages[:3]):  # Only first 3 pages for Railway
                try:
                    tables = page.extract_tables()
                    
                    for table in tables:
                        if len(table) < 2:
                            continue
                        
                        header = table[0]
                        if not header:
                            continue
                        
                        # Find column indices
                        date_idx = None
                        desc_idx = None
                        amount_idx = None
                        
                        for i, col in enumerate(header):
                            if col and 'date' in str(col).lower():
                                date_idx = i
                            elif col and any(word in str(col).lower() for word in ['desc', 'particular', 'narr']):
                                desc_idx = i
                            elif col and any(word in str(col).lower() for word in ['amount', 'debit', 'credit']):
                                amount_idx = i
                        
                        if None in [date_idx, desc_idx, amount_idx]:
                            continue
                        
                        # Process data rows (limit for Railway)
                        for row in table[1:20]:
                            try:
                                if not row or len(row) <= max(date_idx, desc_idx, amount_idx):
                                    continue
                                
                                date = parse_date_robust(str(row[date_idx]))
                                description = str(row[desc_idx])
                                amount = clean_amount_robust(str(row[amount_idx]))
                                
                                if amount != 0 and description.strip():
                                    category, subcategory, trans_type, confidence = enhanced_categorize_transaction(description, amount)
                                    
                                    transaction = ProcessedTransaction(
                                        id=str(uuid.uuid4()),
                                        date=date,
                                        description=description,
                                        amount=amount,
                                        category=category,
                                        type=trans_type,
                                        subcategory=subcategory,
                                        source_file=filename,
                                        confidence_score=confidence
                                    )
                                    
                                    transactions.append(transaction)
                            except:
                                continue
                
                except Exception as e:
                    logger.warning(f"Error processing page {page_num}: {e}")
                    continue
        
        return transactions
        
    except Exception as e:
        raise ValueError(f"PDF processing failed: {str(e)}")

async def process_file_async(file_content: bytes, filename: str) -> List[ProcessedTransaction]:
    """Async file processing"""
    def process_file_sync():
        try:
            if filename.lower().endswith('.csv'):
                return process_csv_optimized(file_content, filename)
            else:
                return process_pdf_optimized(file_content, filename)
        except Exception as e:
            logger.error(f"File processing failed for {filename}: {e}")
            return []
    
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=1) as executor:  # Single worker for Railway
        return await loop.run_in_executor(executor, process_file_sync)

def detect_recurring_transactions(transactions: List[ProcessedTransaction]) -> List[ProcessedTransaction]:
    """Detect recurring transactions"""
    if len(transactions) < 3:
        return transactions
    
    # Group by normalized description and amount
    transaction_groups = {}
    
    for trans in transactions:
        normalized_desc = re.sub(r'\d+', '', trans.description.lower())[:30]
        normalized_desc = re.sub(r'[^\w\s]', ' ', normalized_desc)
        normalized_desc = ' '.join(normalized_desc.split())
        
        amount_bucket = round(abs(trans.amount) / 1000) * 1000
        key = (normalized_desc, amount_bucket, trans.type.value)
        
        if key not in transaction_groups:
            transaction_groups[key] = []
        transaction_groups[key].append(trans)
    
    # Mark as recurring if appears 3+ times
    for group in transaction_groups.values():
        if len(group) >= 3:
            dates = [datetime.strptime(t.date, '%Y-%m-%d') for t in group]
            date_range = (max(dates) - min(dates)).days
            
            if date_range > 30:  # Spread over at least a month
                for trans in group:
                    trans.is_recurring = True
                    trans.confidence_score = min(trans.confidence_score + 0.1, 1.0)
    
    return transactions

def analyze_for_cibil(transactions: List[ProcessedTransaction]) -> Dict[str, Any]:
    """CIBIL analysis"""
    emi_transactions = [t for t in transactions if t.type == TransactionType.EMI]
    cc_transactions = [t for t in transactions if t.type == TransactionType.CREDIT_CARD]
    
    # Monthly EMI calculation
    if emi_transactions:
        unique_months = len(set(t.date[:7] for t in emi_transactions))
        total_emi = sum(abs(t.amount) for t in emi_transactions)
        monthly_emi = total_emi / max(unique_months, 1)
    else:
        monthly_emi = 0.0
    
    # Loan analysis
    loan_types = set()
    for t in emi_transactions:
        if t.subcategory:
            loan_types.add(t.subcategory)
    
    # Credit card behavior
    cc_payments = sum(abs(t.amount) for t in cc_transactions if 'payment' in t.description.lower())
    cc_bills = sum(abs(t.amount) for t in cc_transactions if 'bill' in t.description.lower())
    
    return {
        'monthly_emi_burden': round(monthly_emi, 2),
        'active_loans': list(loan_types),
        'total_emi_paid': round(sum(abs(t.amount) for t in emi_transactions), 2),
        'cc_payment_behavior': {
            'total_payments': round(cc_payments, 2),
            'total_bills': round(cc_bills, 2),
            'payment_ratio': round(cc_payments / max(cc_bills, 1), 2)
        },
        'recurring_payments': len([t for t in transactions if t.is_recurring and t.type in [TransactionType.EMI, TransactionType.CREDIT_CARD]]),
        'payment_consistency': round(len([t for t in emi_transactions if t.is_recurring]) / max(len(emi_transactions), 1), 2)
    }

def analyze_for_tax(transactions: List[ProcessedTransaction]) -> Dict[str, Any]:
    """Tax analysis"""
    income_transactions = [t for t in transactions if t.type == TransactionType.INCOME]
    investment_transactions = [t for t in transactions if t.type == TransactionType.INVESTMENT]
    
    # Annual income estimation
    salary_transactions = [t for t in income_transactions if t.subcategory == 'Salary']
    if salary_transactions:
        unique_months = len(set(t.date[:7] for t in salary_transactions))
        monthly_salary = sum(t.amount for t in salary_transactions) / max(unique_months, 1)
        estimated_annual_income = monthly_salary * 12
    else:
        monthly_salary = 0
        estimated_annual_income = 0
    
    # Tax-saving investments
    tax_saving_80c = sum(abs(t.amount) for t in investment_transactions if t.subcategory in ['Tax_Saving', 'PF_PPF'])
    insurance_premiums = sum(abs(t.amount) for t in transactions if t.category == 'Insurance')
    
    return {
        'estimated_annual_income': round(estimated_annual_income, 2),
        'monthly_salary': round(monthly_salary, 2),
        'tax_saving_investments': {
            '80c_investments': round(tax_saving_80c, 2),
            'insurance_premiums': round(insurance_premiums, 2),
            'total_deductions': round(tax_saving_80c + insurance_premiums, 2)
        },
        'investment_categories': {
            cat: round(sum(abs(t.amount) for t in investment_transactions if t.subcategory == cat), 2)
            for cat in set(t.subcategory for t in investment_transactions if t.subcategory)
        },
        'other_income': round(sum(t.amount for t in income_transactions if t.subcategory != 'Salary'), 2)
    }

# Background cleanup
def cleanup_old_sessions():
    """Background cleanup"""
    while True:
        try:
            time.sleep(300)  # 5 minutes
            current_time = datetime.now()
            to_delete = []
            
            for session_id, data in list(PROCESSED_DATA_STORE.items()):
                if hasattr(data, 'created_at'):
                    created_time = datetime.fromisoformat(data.created_at)
                    if (current_time - created_time).seconds > 1800:  # 30 minutes
                        to_delete.append(session_id)
            
            for session_id in to_delete:
                PROCESSED_DATA_STORE.pop(session_id, None)
                PROCESSING_STATUS.pop(session_id, None)
            
            if to_delete:
                logger.info(f"Cleaned up {len(to_delete)} old sessions")
                
        except Exception as e:
            logger.error(f"Cleanup failed: {e}")

# Start cleanup thread
cleanup_thread = threading.Thread(target=cleanup_old_sessions, daemon=True)
cleanup_thread.start()

# API Endpoints
@app.post("/process-files")
async def process_files(files: List[UploadFile] = File(...)):
    """Main processing endpoint"""
    
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    
    if len(files) > MAX_FILES:
        raise HTTPException(status_code=400, detail=f"Maximum {MAX_FILES} files allowed")
    
    session_id = str(uuid.uuid4())
    PROCESSING_STATUS[session_id] = "processing"
    start_time = time.time()
    
    try:
        logger.info(f"Processing {len(files)} files for session {session_id}")
        
        # Validate and read files
        file_contents = []
        processing_errors = []
        
        for file in files:
            try:
                validate_uploaded_file(file)
                content = await file.read()
                file_contents.append((content, file.filename))
            except Exception as e:
                error_msg = f"File validation failed for {file.filename}: {str(e)}"
                processing_errors.append(error_msg)
                continue
        
        if not file_contents:
            raise HTTPException(status_code=400, detail="No valid files to process")
        
        # Process files
        tasks = [process_file_async(content, filename) for content, filename in file_contents]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Combine results
        all_transactions = []
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                processing_errors.append(f"Error in {file_contents[i][1]}: {str(result)}")
            else:
                all_transactions.extend(result)
        
        if not all_transactions:
            raise HTTPException(status_code=400, detail="No valid transactions found")
        
        # Detect recurring transactions
        all_transactions = detect_recurring_transactions(all_transactions)
        
        # Sort by date
        all_transactions.sort(key=lambda x: x.date)
        
        # Calculate summary
        total_income = sum(t.amount for t in all_transactions if t.type == TransactionType.INCOME)
        total_expense = sum(abs(t.amount) for t in all_transactions if t.type == TransactionType.EXPENSE)
        
        summary = {
            'total_income': round(total_income, 2),
            'total_expense': round(total_expense, 2),
            'net_savings': round(total_income - total_expense, 2),
            'transaction_count': len(all_transactions),
            'file_count': len(file_contents),
            'date_range': {
                'start': min(t.date for t in all_transactions),
                'end': max(t.date for t in all_transactions)
            },
            'processing_time': round(time.time() - start_time, 2)
        }
        
        # Analyses
        credit_behavior = analyze_for_cibil(all_transactions)
        tax_relevant_data = analyze_for_tax(all_transactions)
        
        # Income analysis
        income_transactions = [t for t in all_transactions if t.type == TransactionType.INCOME]
        income_analysis = {
            'total_income': round(total_income, 2),
            'monthly_average': round(total_income / max(len(set(t.date[:7] for t in all_transactions)), 1), 2),
            'income_stability': len([t for t in income_transactions if t.is_recurring]),
        }
        
        # Expense analysis
        expense_by_category = {}
        expense_transactions = [t for t in all_transactions if t.type == TransactionType.EXPENSE]
        for t in expense_transactions:
            cat = t.category
            expense_by_category[cat] = expense_by_category.get(cat, 0) + abs(t.amount)
        
        expense_analysis = {
            'total_expense': round(total_expense, 2),
            'by_category': expense_by_category,
            'top_categories': sorted(expense_by_category.items(), key=lambda x: x[1], reverse=True)[:5]
        }
        
        # Create processed data
        processed_data = ProcessedFinancialData(
            session_id=session_id,
            summary=summary,
            transactions=all_transactions,
            income_analysis=income_analysis,
            expense_analysis=expense_analysis,
            credit_behavior=credit_behavior,
            tax_relevant_data=tax_relevant_data,
            processing_errors=processing_errors,
            processing_warnings=[],
            created_at=datetime.now().isoformat()
        )
        
        PROCESSED_DATA_STORE[session_id] = processed_data
        PROCESSING_STATUS[session_id] = "completed"
        
        logger.info(f"Processing completed for session {session_id}")
        
        return processed_data.to_json()
        
    except Exception as e:
        PROCESSING_STATUS[session_id] = "failed"
        logger.error(f"Processing failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.get("/cibil-data/{session_id}")
async def get_cibil_data(session_id: str):
    """CIBIL teammate endpoint - Returns credit-relevant data"""
    
    if session_id not in PROCESSED_DATA_STORE:
        raise HTTPException(status_code=404, detail="Session not found or expired")
    
    data = PROCESSED_DATA_STORE[session_id]
    
    # Filter CIBIL-relevant transactions
    cibil_transactions = [
        t.to_dict() for t in data.transactions 
        if t.type in [TransactionType.EMI, TransactionType.CREDIT_CARD]
    ]
    
    # Add risk analysis
    risk_indicators = []
    if data.credit_behavior.get('payment_ratio', 1.0) < 0.8:
        risk_indicators.append("Low credit card payment ratio")
    
    if data.credit_behavior.get('monthly_emi_burden', 0) > data.income_analysis.get('monthly_average', 0) * 0.5:
        risk_indicators.append("High EMI burden (>50% of income)")
    
    return {
        'session_id': session_id,
        'credit_behavior': data.credit_behavior,
        'relevant_transactions': cibil_transactions,
        'risk_indicators': risk_indicators,
        'summary': {
            'total_credit_transactions': len(cibil_transactions),
            'emi_transactions': len([t for t in cibil_transactions if t['type'] == 'emi']),
            'cc_transactions': len([t for t in cibil_transactions if t['type'] == 'credit_card']),
            'monthly_obligation': round(data.credit_behavior.get('monthly_emi_burden', 0), 2)
        },
        'recommendations': {
            'maintain_payment_ratio': data.credit_behavior.get('payment_ratio', 1.0) >= 0.9,
            'emi_burden_acceptable': data.credit_behavior.get('monthly_emi_burden', 0) <= data.income_analysis.get('monthly_average', 0) * 0.4,
            'payment_consistency_good': data.credit_behavior.get('payment_consistency', 0) >= 0.8
        }
    }

@app.get("/tax-data/{session_id}")
async def get_tax_data(session_id: str):
    """Tax teammate endpoint - Returns tax-relevant data"""
    
    if session_id not in PROCESSED_DATA_STORE:
        raise HTTPException(status_code=404, detail="Session not found or expired")
    
    data = PROCESSED_DATA_STORE[session_id]
    
    income_transactions = [t.to_dict() for t in data.transactions if t.type == TransactionType.INCOME]
    investment_transactions = [t.to_dict() for t in data.transactions if t.type == TransactionType.INVESTMENT]
    
    # Calculate potential tax savings
    current_80c = data.tax_relevant_data['tax_saving_investments']['80c_investments']
    max_80c = 150000  # Current limit
    remaining_80c = max(0, max_80c - current_80c)
    
    return {
        'session_id': session_id,
        'tax_relevant_data': data.tax_relevant_data,
        'income_analysis': data.income_analysis,
        'income_transactions': income_transactions,
        'investment_transactions': investment_transactions,
        'deduction_eligible_expenses': [
            t.to_dict() for t in data.transactions 
            if t.subcategory and ('tax' in t.subcategory.lower() or t.category in ['Insurance', 'Investment'])
        ],
        'tax_optimization': {
            'remaining_80c_limit': remaining_80c,
            'potential_tax_saving': round(remaining_80c * 0.3, 2),  # Assuming 30% tax bracket
            'current_deductions': round(current_80c + data.tax_relevant_data['tax_saving_investments']['insurance_premiums'], 2),
            'recommendations': {
                'increase_80c_investments': remaining_80c > 50000,
                'consider_nps': remaining_80c < 50000,
                'health_insurance_adequate': data.tax_relevant_data['tax_saving_investments']['insurance_premiums'] >= 25000
            }
        },
        'projected_tax_liability': {
            'gross_income': data.tax_relevant_data['estimated_annual_income'],
            'total_deductions': current_80c + data.tax_relevant_data['tax_saving_investments']['insurance_premiums'],
            'taxable_income': max(0, data.tax_relevant_data['estimated_annual_income'] - current_80c - data.tax_relevant_data['tax_saving_investments']['insurance_premiums'] - 50000),  # Basic exemption
            'estimated_tax': max(0, (data.tax_relevant_data['estimated_annual_income'] - current_80c - data.tax_relevant_data['tax_saving_investments']['insurance_premiums'] - 50000) * 0.2)  # Simplified calculation
        }
    }

@app.get("/processing-status/{session_id}")
async def get_processing_status(session_id: str):
    """Status check endpoint"""
    status = PROCESSING_STATUS.get(session_id, "not_found")
    
    response = {
        "session_id": session_id, 
        "status": status,
        "timestamp": datetime.now().isoformat()
    }
    
    if status == "completed":
        if session_id in PROCESSED_DATA_STORE:
            data = PROCESSED_DATA_STORE[session_id]
            response["summary"] = {
                "transaction_count": len(data.transactions),
                "processing_time": data.summary.get('processing_time', 0),
                "total_income": data.summary.get('total_income', 0),
                "total_expense": data.summary.get('total_expense', 0)
            }
        else:
            response["status"] = "expired"
    
    return response

@app.get("/session-data/{session_id}")
async def get_session_data(session_id: str):
    """Get complete session data"""
    
    if session_id not in PROCESSED_DATA_STORE:
        raise HTTPException(status_code=404, detail="Session not found or expired")
    
    data = PROCESSED_DATA_STORE[session_id]
    return data.to_json()

@app.delete("/session/{session_id}")
async def delete_session(session_id: str):
    """Delete session data"""
    
    PROCESSED_DATA_STORE.pop(session_id, None)
    PROCESSING_STATUS.pop(session_id, None)
    
    return {"message": f"Session {session_id} deleted successfully"}

@app.get("/health")
async def health_check():
    """Basic health check"""
    return {
        "status": "healthy",
        "active_sessions": len(PROCESSED_DATA_STORE),
        "processing_queue": len([s for s in PROCESSING_STATUS.values() if s == "processing"]),
        "version": "2.2.0",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "service": "Financial Data Processing Hub - Railway Ready",
        "version": "2.2.0",
        "status": "running",
        "description": "Process financial data (CSV/PDF) and extract insights for CIBIL and tax analysis",
        "endpoints": {
            "process_files": "POST /process-files (Upload CSV/PDF files)",
            "cibil_data": "GET /cibil-data/{session_id} (Credit behavior analysis)",
            "tax_data": "GET /tax-data/{session_id} (Tax optimization insights)",
            "session_data": "GET /session-data/{session_id} (Complete processed data)",
            "status": "GET /processing-status/{session_id} (Check processing status)",
            "delete_session": "DELETE /session/{session_id} (Clean up session)",
            "health": "GET /health (API health status)"
        },
        "limits": {
            "max_file_size": f"{MAX_FILE_SIZE/1024/1024}MB",
            "max_files": MAX_FILES,
            "supported_formats": list(ALLOWED_EXTENSIONS)
        }
    }

# Railway deployment optimization
@app.on_event("startup")
async def startup_event():
    """Application startup"""
    logger.info("🚀 Financial Data Processing Hub starting up...")
    logger.info(f"📊 Max file size: {MAX_FILE_SIZE/1024/1024}MB")
    logger.info(f"📁 Max files: {MAX_FILES}")
    logger.info("✅ Railway optimization enabled")
    logger.info("🔄 Background cleanup started")
    logger.info("🎯 Ready to process financial data!")

if __name__ == "__main__":
    import uvicorn
    
    # Railway uses PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    
    logger.info("🚀 Starting Financial Data Processing Hub for Railway...")
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        log_level="info"
    )