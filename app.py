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

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            padding-top: 2rem;
        }
        .stChatMessage {
            padding: 1rem;
            border-radius: 0.5rem;
        }
        .topic-badge {
            background-color: #1f77b4;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 0.25rem;
            display: inline-block;
            margin: 0.25rem;
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

# Header Section
st.title("🐍 PyGuide AI: Smart Python Learning Engine")
st.caption(
    "Learn Python concepts interactively with real-life examples and code snippets. "
    "Built as part of DecodeLab AI Internship."
)

# Two-column layout
col1, col2 = st.columns([2, 1], gap="medium")

with col2:
    st.subheader("📚 Topics Explorer")
    st.markdown("---")
    with st.container(border=True):
        st.markdown(f"**Total Topics:** {len(knowledge_base)}")
        st.markdown("**Available Topics:**")
        for i, topic in enumerate(knowledge_base.keys(), 1):
            st.markdown(f"  {i}. `{topic.title()}`")


# Initialize Chat History
with col1:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """
🤖 **Welcome to PyGuide AI!**

I'm your intelligent Python learning assistant. I can help you understand:
- **Basic Concepts**: Variables, Data Types, Strings
- **Collections**: Lists, Tuples, Dictionaries, Sets
- **Control Flow**: If statements, Loops
- **Functions & OOP**: Functions, Classes, Decorators, Generators
- **Advanced Topics**: Exception Handling, File I/O, JSON, Modules

✨ **How to use me:**
1. Ask me about any Python concept
2. I'll provide a definition, real-life example, and code syntax
3. Type a topic name like "variable", "function", "loop", etc.

🎯 Start by asking me about any Python topic!
                """,
            }
        ]

    # Display Previous Messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input
    if user_input := st.chat_input("Ask me about any Python topic..."):
        # Add user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )
        
        with st.chat_message("user"):
            st.markdown(user_input)

        # Process input and generate response
        with st.chat_message("assistant"):
            result = find_matching_topic(user_input, knowledge_base)
            
            if result:
                topic, data = result
                bot_response = format_response(topic, data)
            else:
                bot_response = f"""
❌ **Hmm, I don't know about that yet!**

The topic you're asking about isn't in my knowledge base yet. 

📝 **Available topics include:**
{', '.join([f'`{topic.title()}`' for topic in list(knowledge_base.keys())[:10]])}
...and more!

💡 Try asking about any Python concept from the list above, or check the "Topics Explorer" on the right.
"""
            
            st.markdown(bot_response)
            st.session_state.messages.append(
                {"role": "assistant", "content": bot_response}
            )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
        <p>PyGuide AI v1.0.0 | Built with ❤️ during DecodeLab AI Internship</p>
        <p>For more topics and features, visit our <a href='https://github.com'>GitHub Repository</a></p>
    </div>
    """,
    unsafe_allow_html=True
)