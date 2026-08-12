"""
PyGuide AI - Streamlit Web Application
An interactive AI chatbot for learning Python concepts

Author: Farhan (DecodeLab Internship)
Version: 1.0.0

This application provides an intuitive web interface for exploring Python 
concepts with real-life examples and code snippets.
"""

import json
import streamlit as st
from typing import Dict, Any, Optional


# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="PyGuide AI",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
        /* Main Container */
        .main {
            padding-top: 1rem;
            background-color: #f8f9fa;
        }
        
        /* Chat Messages */
        .stChatMessage {
            padding: 1.2rem;
            border-radius: 0.75rem;
            margin-bottom: 0.5rem;
            background-color: white;
            border-left: 4px solid #1f77b4;
        }
        
        /* Header Styling */
        .header-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem 1.5rem;
            border-radius: 1rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .header-container h1 {
            margin: 0;
            font-size: 2.5rem;
            font-weight: 700;
        }
        
        .header-container p {
            margin-top: 0.5rem;
            font-size: 1.1rem;
            opacity: 0.95;
        }
        
        /* Metrics Cards */
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 0.75rem;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
            border-top: 3px solid #667eea;
        }
        
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
            margin: 0.5rem 0;
        }
        
        .metric-label {
            color: #666;
            font-size: 0.9rem;
            font-weight: 500;
        }
        
        /* Topic Badge */
        .topic-badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.6rem 1.2rem;
            border-radius: 0.5rem;
            display: inline-block;
            margin: 0.3rem;
            font-weight: 500;
            box-shadow: 0 2px 4px rgba(102, 126, 234, 0.3);
        }
        
        /* Sidebar */
        .sidebar {
            background-color: white;
        }
        
        /* Features Section */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            margin: 1rem 0;
        }
        
        .feature-item {
            background: white;
            padding: 1rem;
            border-radius: 0.5rem;
            border-left: 3px solid #667eea;
            font-size: 0.9rem;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            color: #666;
            font-size: 0.85rem;
            padding: 2rem 0 1rem;
            border-top: 1px solid #ddd;
            margin-top: 2rem;
        }
        
        /* Input Area */
        .stChatInput {
            background-color: white;
            border: 2px solid #e0e0e0;
            border-radius: 0.75rem;
            padding: 1rem;
        }
        
        /* Links */
        a {
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }
        
        a:hover {
            text-decoration: underline;
            color: #764ba2;
        }
    </style>
""", unsafe_allow_html=True)


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

@st.cache_data
def load_knowledge_base(filepath: str = "intents.json") -> Dict[str, Any]:
    """
    Load the knowledge base from intents.json file.
    
    Args:
        filepath (str): Path to the intents.json file
        
    Returns:
        Dict[str, Any]: Knowledge base dictionary
        
    Raises:
        FileNotFoundError: If intents.json is not found
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"❌ '{filepath}' file not found! Please ensure it's in the application directory."
        )
    except json.JSONDecodeError:
        raise ValueError(f"❌ '{filepath}' is not a valid JSON file!")


def find_matching_topic(user_input: str, knowledge_base: Dict[str, Any]) -> Optional[tuple]:
    """
    Find a matching topic from the knowledge base.
    
    Args:
        user_input (str): User's query text
        knowledge_base (Dict[str, Any]): Knowledge base dictionary
        
    Returns:
        Optional[tuple]: (topic_name, topic_data) if found, None otherwise
    """
    user_input_lower = user_input.lower().strip()
    
    # Direct match
    if user_input_lower in knowledge_base:
        return user_input_lower, knowledge_base[user_input_lower]
    
    # Substring matching
    for topic, data in knowledge_base.items():
        if topic in user_input_lower:
            return topic, data
    
    return None


def format_response(topic: str, data: Dict[str, Any]) -> str:
    """
    Format the topic response into a nice markdown string.
    
    Args:
        topic (str): Topic name
        data (Dict[str, Any]): Topic data
        
    Returns:
        str: Formatted markdown response
    """
    response = f"""
### 📌 **Topic: {topic.title()}**

**📖 Definition:**
> {data.get('definition', 'Definition not available')}

---

**💡 Real-Life Example:**
> {data.get('example', 'Example not available')}

---

**💻 Code Syntax:**
```python
{data.get('syntax', 'Syntax not available')}
```
"""
    return response


# ============================================================================
# LOAD KNOWLEDGE BASE
# ============================================================================

try:
    knowledge_base = load_knowledge_base()
except (FileNotFoundError, ValueError) as e:
    st.error(str(e))
    st.info("💡 Please ensure 'intents.json' is in the application directory.")
    st.stop()


# ============================================================================
# PAGE LAYOUT
# ============================================================================

# Professional Header
st.markdown("""
<div class="header-container">
    <h1>🐍 PyGuide AI</h1>
    <p>Smart Python Learning Engine - Learn Python Interactively!</p>
</div>
""", unsafe_allow_html=True)

# Metrics Row
st.subheader("📊 Dashboard Overview")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">📚 Topics Available</div>
        <div class="metric-value">{len(knowledge_base)}</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">💻 Code Examples</div>
        <div class="metric-value">{len(knowledge_base)}</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🎯 Coverage</div>
        <div class="metric-value">100%</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">⭐ Beginner Friendly</div>
        <div class="metric-value">✓</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Two-column layout
col1, col2 = st.columns([2.5, 1.2], gap="medium")

# ============================================================================
# SIDEBAR - ENHANCED
# ============================================================================

with st.sidebar:
    st.markdown("### 🎓 Quick Access")
    st.markdown("---")
    
    # Search functionality
    search_query = st.text_input(
        "🔍 Search topics:",
        placeholder="e.g., variable, function, list...",
        help="Search for Python topics"
    )
    
    st.markdown("---")
    st.markdown("### 📚 All Topics")
    
    with st.container(border=True):
        topics_list = list(knowledge_base.keys())
        
        # Filter topics based on search
        if search_query:
            filtered_topics = [t for t in topics_list if search_query.lower() in t.lower()]
        else:
            filtered_topics = topics_list
        
        for i, topic in enumerate(filtered_topics, 1):
            col_btn, col_num = st.columns([0.85, 0.15])
            with col_btn:
                if st.button(
                    f"📌 {topic.title()}",
                    key=f"topic_{topic}",
                    use_container_width=True,
                    help=f"Learn about {topic}"
                ):
                    st.session_state.selected_topic = topic
            with col_num:
                st.caption(str(i))
    
    st.markdown("---")
    
    # About Section
    st.markdown("### 📖 About This App")
    st.info("""
    **PyGuide AI** is an interactive Python learning platform built during the **DecodeLab AI Internship**.
    
    **Features:**
    - 20+ Python topics
    - Real-life examples
    - Practical code snippets
    - AI-powered explanations
    
    **Creator:** Farhan  
    **Version:** 1.0.0  
    **License:** MIT
    """)
    
    st.markdown("---")
    
    # Links
    col_github, col_code = st.columns(2)
    with col_github:
        st.link_button(
            "💻 GitHub Repo",
            "https://github.com/Farhanillahiclass/simple_ai_chatbot",
            use_container_width=True
        )
    with col_code:
        st.link_button(
            "🐍 Python.org",
            "https://www.python.org",
            use_container_width=True
        )


# ============================================================================
# MAIN CONTENT AREA
# ============================================================================

with col1:
    st.markdown("### 💬 Chat with PyGuide AI")
    st.markdown("---")


# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
🤖 **Welcome to PyGuide AI!**

I'm your intelligent Python learning assistant, powered by AI to help you master Python concepts! 

### 📚 What I Can Teach You:
- **Basics**: Variables, Data Types, Strings, Slicing
- **Collections**: Lists, Tuples, Dictionaries, Sets
- **Control Flow**: If Statements, Loops (for, while)
- **Functions**: Function definition, Lambda, Decorators, Generators
- **OOP**: Classes, Inheritance, OOP Principles
- **Advanced**: Exception Handling, File I/O, JSON, Modules, Map/Filter/Reduce

### 💡 How to Use:
1. **Type a topic** in the chat box (e.g., "variable", "function", "list")
2. **I'll explain** the concept with a clear definition
3. **See examples** with real-life use cases
4. **Get code** snippets you can use immediately

### 🎯 Try These Topics:
`variable` • `list` • `function` • `loop` • `class` • `dictionary`

---

**Let's start learning!** What Python topic interests you? 🐍✨
            """,
        }
    ]

# Display Previous Messages with Better Styling
st.container(height=400, border=False)
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🤖" if message["role"] == "assistant" else "👤"):
        st.markdown(message["content"])

# User Input
if user_input := st.chat_input(
    "💬 Ask me about any Python topic... (e.g., 'variable', 'function', 'list')",
    key="chat_input"
):
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    # Process input and generate response
    with st.chat_message("assistant", avatar="🤖"):
        result = find_matching_topic(user_input, knowledge_base)
        
        if result:
            topic, data = result
            bot_response = format_response(topic, data)
            st.success("✅ Found topic! Here's the explanation:")
        else:
            # Show suggestions
            suggestions = [t.title() for t in list(knowledge_base.keys())[:8]]
            bot_response = f"""
❌ **Hmm, I don't know about that yet!**

The topic you're asking about isn't in my knowledge base. Let me help you find what you're looking for!

### 💡 **Suggested Topics:**
{' • '.join([f'`{s}`' for s in suggestions])}

### 📖 **Pro Tips:**
- Use simple topic names (e.g., "variable" instead of "what is a variable")
- Check the sidebar for a complete list of available topics
- Use the search feature to find topics quickly

Try asking about one of the suggestions above! 🔍
"""
            st.warning("Topic not found! Showing suggestions...")
        
        st.markdown(bot_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_response}
        )

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div class="footer">
    <h4>🐍 PyGuide AI v1.0.0</h4>
    <p>
        <strong>Smart Python Learning Engine</strong> | 
        Built with ❤️ during <strong>DecodeLab AI Internship</strong>
    </p>
    
    <p>
        <a href="https://github.com/Farhanillahiclass/simple_ai_chatbot">📍 GitHub Repository</a> • 
        <a href="https://www.python.org">🐍 Python.org</a> • 
        <a href="https://streamlit.io">🎯 Streamlit</a>
    </p>
    
    <p style="font-size: 0.8rem; margin-top: 1rem; opacity: 0.7;">
        Created by: Farhan | License: MIT | 
        Made with Python 🐍 + Streamlit 🎯 + Love ❤️
    </p>
</div>
""", unsafe_allow_html=True)