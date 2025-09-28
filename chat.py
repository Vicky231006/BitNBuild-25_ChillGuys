import streamlit as st
import google.generativeai as genai
import os
import json
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration and Data Loading ---

# JSON file ka naam define karein
JSON_FILE = 'response.json'

@st.cache_data
def load_rag_data(file_path):
    """
    Load financial RAG data from response.json file and create searchable knowledge base
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Create a knowledge base from your financial data
        knowledge_base = {}
        
        if 'cibil_summary' in data:
            cibil = data['cibil_summary']
            # CIBIL related queries
            knowledge_base['what is my cibil score'] = f"Your CIBIL score is {cibil['cibil_score']} which is {cibil['status']}."
            knowledge_base['my credit score'] = f"Your credit score is {cibil['cibil_score']} ({cibil['status']})."
            knowledge_base['what is my emi'] = f"Your monthly EMI is {cibil['credit_metrics']['monthly_emi']}."
            knowledge_base['my monthly emi'] = f"Your monthly EMI is {cibil['credit_metrics']['monthly_emi']}."
            knowledge_base['debt to income ratio'] = f"Your debt-to-income ratio is {cibil['credit_metrics']['debt_to_income_pct']}."
            knowledge_base['credit utilization'] = f"Your credit utilization is {cibil['credit_metrics']['credit_utilization_pct']}."
            knowledge_base['credit limit'] = f"Your estimated credit limit is {cibil['credit_metrics']['estimated_credit_limit']}."
            knowledge_base['credit advice'] = cibil['key_advice']
        
        if 'tax_summary' in data:
            tax = data['tax_summary']
            # Tax related queries
            knowledge_base['my annual income'] = f"Your annual income is ₹{tax['annual_income']:,}."
            knowledge_base['my monthly income'] = f"Your monthly income is ₹{tax['monthly_income']:,}."
            knowledge_base['tax regime recommendation'] = f"Recommended tax regime: {tax['recommended_tax_regime']}."
            knowledge_base['tax savings'] = f"Annual tax savings with new regime: ₹{tax['annual_tax_savings_with_new_regime']:,}."
            knowledge_base['old vs new regime'] = f"Old regime tax: ₹{tax['tax_burden_comparison']['old_regime_tax']:,}, New regime tax: ₹{tax['tax_burden_comparison']['new_regime_tax']:,}."
            knowledge_base['current deductions'] = f"Current deductions claimed: ₹{tax['current_deductions_claimed']:,}."
        
        if 'financial_context' in data:
            context = data['financial_context']
            # Financial context queries
            knowledge_base['income sources'] = context['key_income_sources']
            knowledge_base['my income sources'] = context['key_income_sources']
            knowledge_base['debt obligations'] = context['monthly_debt_obligations_detail']
            knowledge_base['monthly debt'] = context['monthly_debt_obligations_detail']
            knowledge_base['tax recommendation reason'] = context['tax_recommendation_reasoning']
            knowledge_base['dti details'] = context['dti_note']
        
        # Add session info
        if 'session_id' in data:
            knowledge_base['session id'] = f"Your session ID is {data['session_id']}."
        
        return knowledge_base
            
    except FileNotFoundError:
        st.warning(f"Warning: RAG file '{file_path}' not found. Chatbot will use only Gemini API.")
        return {}
    except json.JSONDecodeError:
        st.error(f"Error: The file '{file_path}' is not a valid JSON file. Please check its format.")
        return {}
    except Exception as e:
        st.error(f"An unexpected error occurred during RAG data loading: {str(e)}")
        return {}

# Configure page with a custom theme
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Solid and Clean CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

/* Global Reset and Hide Streamlit Elements */
#MainMenu, footer, header, .stDeployButton, .stDecoration, 
.stToolbar, [data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0 !important;
    display: none !important;
}

* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    box-sizing: border-box;
}

/* Root Container */
.stApp {
    background: #0f1419 !important;
}

.main {
    background: #0f1419 !important;
    min-height: 100vh;
    padding: 0 !important;
    margin: 0 !important;
}

.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: none !important;
    width: 100% !important;
}

/* Header Section */
.chat-header {
    background: #1a1f2e;
    border-bottom: 1px solid #2a2f3e;
    padding: 24px;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 100;
}

.chat-title {
    font-size: 28px;
    font-weight: 600;
    color: #ffffff;
    margin: 0 0 8px 0;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
}

.chat-subtitle {
    color: #9ca3af;
    font-size: 14px;
    font-weight: 400;
    margin: 0;
}

/* Chat Container */
.chat-container {
    max-width: 800px;
    margin: 0 auto;
    min-height: calc(100vh - 120px);
    display: flex;
    flex-direction: column;
    padding: 20px;
}

/* Message Styling */
[data-testid="stChatMessage"] {
    margin: 12px 0 !important;
    display: flex !important;
    align-items: flex-end !important;
    width: 100% !important;
    max-width: 100% !important;
}

/* User Messages (Right Side) */
[data-testid="stChatMessage"][data-testid*="user"] {
    justify-content: flex-end !important;
}

[data-testid="stChatMessage"][data-testid*="user"] > div:first-child {
    order: 2;
    margin-left: 12px !important;
}

[data-testid="stChatMessage"][data-testid*="user"] > div:last-child {
    order: 1;
    background: #3b82f6 !important;
    color: #ffffff !important;
    border-radius: 18px 18px 6px 18px !important;
    padding: 12px 16px !important;
    max-width: 70% !important;
    font-size: 15px !important;
    font-weight: 400 !important;
    line-height: 1.5 !important;
    box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3) !important;
    border: none !important;
    margin: 0 !important;
}

/* Assistant Messages (Left Side) */
[data-testid="stChatMessage"]:not([data-testid*="user"]) {
    justify-content: flex-start !important;
}

[data-testid="stChatMessage"]:not([data-testid*="user"]) > div:first-child {
    order: 1;
    margin-right: 12px !important;
}

[data-testid="stChatMessage"]:not([data-testid*="user"]) > div:last-child {
    order: 2;
    background: #1f2937 !important;
    color: #ffffff !important;
    border-radius: 18px 18px 18px 6px !important;
    padding: 12px 16px !important;
    max-width: 70% !important;
    font-size: 15px !important;
    font-weight: 400 !important;
    line-height: 1.5 !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
    border: 1px solid #374151 !important;
    margin: 0 !important;
}

/* Avatar Styling */
[data-testid="stChatMessage"] img {
    width: 36px !important;
    height: 36px !important;
    border-radius: 50% !important;
    flex-shrink: 0 !important;
    border: 2px solid #374151 !important;
}

[data-testid="stChatMessage"][data-testid*="user"] img {
    border-color: #3b82f6 !important;
}

/* Input Container */
.stChatFloatingInputContainer {
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    background: #0f1419 !important;
    border-top: 1px solid #2a2f3e !important;
    padding: 16px !important;
    z-index: 1000 !important;
}

.stChatInputContainer {
    max-width: 800px !important;
    margin: 0 auto !important;
    width: 100% !important;
}

.stChatInputContainer > div {
    background: #1f2937 !important;
    border: 1px solid #374151 !important;
    border-radius: 24px !important;
    padding: 4px !important;
    display: flex !important;
    align-items: center !important;
}

.stChatInputContainer textarea {
    background: transparent !important;
    color: #ffffff !important;
    border: none !important;
    font-size: 15px !important;
    font-weight: 400 !important;
    padding: 12px 20px !important;
    border-radius: 20px !important;
    resize: none !important;
    min-height: 20px !important;
    max-height: 120px !important;
    line-height: 1.5 !important;
    flex: 1 !important;
}

.stChatInputContainer textarea::placeholder {
    color: #9ca3af !important;
}

.stChatInputContainer textarea:focus {
    outline: none !important;
    color: #ffffff !important;
}

/* Send Button */
[data-testid="stChatInputSubmitButton"] {
    background: #3b82f6 !important;
    border: none !important;
    border-radius: 50% !important;
    width: 44px !important;
    height: 44px !important;
    margin: 4px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    flex-shrink: 0 !important;
}

[data-testid="stChatInputSubmitButton"]:hover {
    background: #2563eb !important;
    transform: scale(1.05) !important;
}

[data-testid="stChatInputSubmitButton"] svg {
    color: #ffffff !important;
    width: 20px !important;
    height: 20px !important;
}

/* Welcome Screen */
.welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 80px 20px;
    min-height: 400px;
}

.welcome-title {
    font-size: 32px;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 16px;
}

.welcome-subtitle {
    font-size: 16px;
    color: #9ca3af;
    line-height: 1.6;
    max-width: 500px;
}

/* Content Padding for Fixed Input */
.main > div:first-child {
    padding-bottom: 100px !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #1f2937;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: #374151;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #4b5563;
}

/* Loading Spinner */
.stSpinner > div {
    border-top-color: #3b82f6 !important;
}

/* Alert Styling */
.stAlert {
    background: #1f2937 !important;
    color: #ffffff !important;
    border: 1px solid #374151 !important;
    border-radius: 12px !important;
    margin: 16px 0 !important;
}

/* Code Blocks */
pre {
    background: #111827 !important;
    border: 1px solid #374151 !important;
    border-radius: 8px !important;
    padding: 16px !important;
    overflow-x: auto !important;
    margin: 12px 0 !important;
}

code {
    background: #374151 !important;
    color: #f9fafb !important;
    padding: 2px 6px !important;
    border-radius: 4px !important;
    font-size: 13px !important;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .chat-container {
        padding: 16px;
    }
    
    .chat-header {
        padding: 20px 16px;
    }
    
    .chat-title {
        font-size: 24px;
    }
    
    [data-testid="stChatMessage"] > div {
        max-width: 85% !important;
        font-size: 14px !important;
    }
    
    .stChatFloatingInputContainer {
        padding: 12px !important;
    }
    
    .welcome-title {
        font-size: 28px;
    }
    
    .welcome-subtitle {
        font-size: 15px;
    }
}
</style>
""", unsafe_allow_html=True)

class Chatbot:
    def __init__(self):
        """Initialize the chatbot with Gemini API."""
        try:
            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                raise Exception("GEMINI_API_KEY environment variable not found. Check your .env file.")
                
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.5-flash')
            self.chat = self.model.start_chat(history=[])
        except Exception as e:
            raise Exception(f"Failed to initialize Gemini API: {str(e)}")
    
    def generate_response(self, user_input: str) -> str:
        """Generate response from the model."""
        try:
            response = self.chat.send_message(user_input)
            return response.text
        except Exception as e:
            raise Exception(f"Error generating response: {str(e)}")

def main():
    # --- RAG Data Loading ---
    # Load and cache RAG data
    rag_data = load_rag_data(JSON_FILE) 
    
    # Header
    st.markdown("""
    <div class="chat-header">
        <div class="chat-title">
            🤖 AI Chat Assistant
        </div>
        <div class="chat-subtitle">Powered by Gemini AI + RAG • Ask me anything</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main chat container
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Initialize session state
    if 'chatbot' not in st.session_state:
        try:
            st.session_state.chatbot = Chatbot()
        except Exception as e:
            st.error(f"❌ Failed to initialize chatbot: {str(e)}")
            st.info("💡 Please check your API key configuration.")
            st.stop()
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Welcome screen for empty chat
    if not st.session_state.messages:
        rag_status = "✅ RAG Data Loaded" if rag_data else "⚠️ Only AI Mode"
        st.markdown(f"""
        <div class="welcome-container">
            <div class="welcome-title">👋 Welcome!</div>
            <div class="welcome-subtitle">
                I'm your AI assistant with RAG capabilities. I can answer from my knowledge base or use AI.<br>
                Status: {rag_status} | Start a conversation by typing below.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    try:
        # Display chat messages
        for message in st.session_state.messages:
            if message["role"] == "user":
                with st.chat_message("user", avatar="👤"):
                    st.markdown(message["content"])
            else:
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Type your message here...", key="chat_input"):
            # Display user message
            with st.chat_message("user", avatar="👤"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            response = ""
            user_query_clean = prompt.strip().lower()

            # --- Enhanced RAG Logic with Partial Matching ---
            rag_hit = False
            if rag_data:
                # First try exact match
                if user_query_clean in rag_data:
                    response = rag_data[user_query_clean]
                    response += "\n\n*📊 (Source: Your Financial Data)*"
                    rag_hit = True
                else:
                    # Try partial matching for better user experience
                    for key in rag_data.keys():
                        if any(word in user_query_clean for word in key.split() if len(word) > 3):
                            response = rag_data[key]
                            response += "\n\n*📊 (Source: Your Financial Data)*"
                            rag_hit = True
                            break
            
            if rag_hit:
                # Display RAG response immediately
                with st.chat_message("assistant", avatar="🤖"):
                    st.markdown(response)
            else:
                # Fallback to Gemini API with financial context
                with st.chat_message("assistant", avatar="🤖"):
                    with st.spinner("🤔 Analyzing with AI..."):
                        # Add financial context to the prompt for better AI responses
                        enhanced_prompt = f"""
                        User question: {prompt}
                        
                        Context: This user has financial data available including:
                        - CIBIL score and credit information
                        - Tax planning details
                        - Income and debt information
                        
                        Please provide a helpful response. If the question is about their specific financial data and you don't have access to it, suggest they ask specific questions like "what is my CIBIL score" or "my monthly income".
                        """
                        response = st.session_state.chatbot.generate_response(enhanced_prompt)
                    st.markdown(response)

            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Auto-scroll to bottom
            st.rerun()
            
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
        st.info("🔧 Please check your configuration and try again.")
    
    # Close container
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
