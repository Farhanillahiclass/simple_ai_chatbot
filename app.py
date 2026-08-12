import streamlit as st
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="PyGuide AI — Smart Python Learning Engine",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. KNOWLEDGE BASE DATA STRUCTURE
# ==========================================
PYTHON_KNOWLEDGE_BASE = {
    "variables": {
        "title": "Variables & Data Types",
        "category": "Fundamentals",
        "explanation": "Variables are containers for storing data values in Python. Python is dynamically typed.",
        "code": """# Variable Assignment
x = 10                  # Integer
name = "Farhan"          # String
price = 99.99           # Float
is_active = True        # Boolean

print(type(x))         # <class 'int'>"""
    },
    "data types": {
        "title": "Built-in Data Types",
        "category": "Fundamentals",
        "explanation": "Python features rich built-in data types categorized into Numeric, Sequence, Mapping, Set, and Boolean types.",
        "code": """age = 21
greeting = "Hello, Python!"
numbers = [1, 2, 3]
user = {"name": "Farhan", "role": "AI Intern"}"""
    },
    "lists": {
        "title": "Lists & List Methods",
        "category": "Collections",
        "explanation": "Lists are ordered, mutable collections that allow duplicate elements.",
        "code": """fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
uppercase_fruits = [f.upper() for f in fruits]
print(uppercase_fruits)"""
    },
    "dictionaries": {
        "title": "Dictionaries (Key-Value Pairs)",
        "category": "Collections",
        "explanation": "Dictionaries store data values in key:value pairs.",
        "code": """student = {
    "name": "Farhan",
    "course": "AI & Python",
    "internship": "DecodeLab AI"
}
for key, value in student.items():
    print(f"{key}: {value}")"""
    },
    "functions": {
        "title": "Functions & Arguments",
        "category": "Modular Python",
        "explanation": "Functions are reusable blocks of code.",
        "code": """def build_profile(name, *skills):
    return {"name": name, "skills": list(skills)}

user = build_profile("Farhan", "Python", "AI", "Streamlit")
print(user)"""
    },
    "decorators": {
        "title": "Decorators",
        "category": "Advanced",
        "explanation": "Decorators extend function behavior without modifying the original function.",
        "code": """def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello Farhan!")

say_hello()"""
    },
    "oop": {
        "title": "Object-Oriented Programming (OOP)",
        "category": "Advanced",
        "explanation": "OOP structures code around objects and classes.",
        "code": """class AIModel:
    def __init__(self, name):
        self.name = name

bot = AIModel("PyGuide Assistant")
print(bot.name)"""
    },
    "lambda": {
        "title": "Lambda Functions",
        "category": "Functional Python",
        "explanation": "Small anonymous functions defined with the lambda keyword.",
        "code": """square = lambda x: x ** 2
print(square(5))  # Output: 25"""
    }
}

def search_knowledge_base(query):
    query_clean = query.lower().strip()
    for key in PYTHON_KNOWLEDGE_BASE:
        if key in query_clean:
            return PYTHON_KNOWLEDGE_BASE[key]
    for key, data in PYTHON_KNOWLEDGE_BASE.items():
        if query_clean in data["title"].lower() or query_clean in data["category"].lower():
            return data
    return None

# ==========================================
# 3. SIDEBAR SETUP
# ==========================================
with st.sidebar:
    st.title("🐍 PyGuide AI")
    st.caption("Smart Python Learning Engine v1.0")
    st.divider()

    menu = st.radio(
        "Navigation",
        ["Dashboard & Chat", "Browse All Topics", "Project Info"],
        index=0
    )

    st.divider()
    st.subheader("ℹ️ Project Credits")
    st.markdown("""
    - **Internship:** DecodeLab AI Internship
    - **Creator:** Farhan
    - **License:** MIT
    - **Tech:** Python • Streamlit
    """)
    
    st.divider()
    st.markdown("[🌐 GitHub Repository](https://github.com/Farhanillahiclass/simple_ai_chatbot)")

# ==========================================
# 4. MAIN CONTENT AREA
# ==========================================
if menu == "Dashboard & Chat":

    st.title("Welcome to PyGuide AI 👋")
    st.caption("Your intelligent Python learning assistant, powered by structured knowledge bases and instant code explanations.")
    st.divider()

    # Quick Stats Section
    st.subheader("📊 Quick Stats")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Core Topics", value="10+", delta="Beginner to Adv")
    with col2:
        st.metric(label="Code Samples", value="25+", delta="Ready to run")
    with col3:
        st.metric(label="Coverage", value="100%", delta="Python Core")
    with col4:
        st.metric(label="AI Tutor", value="Active", delta="Instant Reply")

    st.divider()

    # Quick Topic Buttons
    st.subheader("💡 Try Asking About These Topics:")
    
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        if st.button("Variables", use_container_width=True):
            st.session_state.selected_prompt = "variables"
    with c2:
        if st.button("Functions", use_container_width=True):
            st.session_state.selected_prompt = "functions"
    with c3:
        if st.button("Decorators", use_container_width=True):
            st.session_state.selected_prompt = "decorators"
    with c4:
        if st.button("OOP Principles", use_container_width=True):
            st.session_state.selected_prompt = "oop"
    with c5:
        if st.button("Lambda", use_container_width=True):
            st.session_state.selected_prompt = "lambda"

    st.divider()

    # Interactive Chat Assistant
    st.subheader("💬 Interactive Chat Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! I am **PyGuide AI**, built by Farhan for the DecodeLab AI Internship. Ask me any Python question (e.g., *'Explain decorators'*, *'How do lists work?'*, or *'Show function example'*)."
            }
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt_input = st.chat_input("Ask a question about Python concepts or syntax...")
    if "selected_prompt" in st.session_state and st.session_state.selected_prompt:
        prompt_input = st.session_state.selected_prompt
        st.session_state.selected_prompt = None

    if prompt_input:
        st.chat_message("user").markdown(prompt_input)
        st.session_state.messages.append({"role": "user", "content": prompt_input})

        match = search_knowledge_base(prompt_input)

        with st.chat_message("assistant"):
            if match:
                st.markdown(f"### 📌 {match['title']} ({match['category']})")
                st.write(match['explanation'])
                st.markdown("#### 💻 Code Example:")
                st.code(match['code'], language="python")
                
                response_text = f"### 📌 {match['title']} ({match['category']})\n\n{match['explanation']}\n\n```python\n{match['code']}\n```"
            else:
                response_text = f"I couldn't find an exact match for **'{prompt_input}'** in my core knowledge base.\n\n### 💡 Try asking about:\n- `variables`, `functions`, `decorators`, `lists`, `dictionaries`, `oop`"
                st.markdown(response_text)

            st.session_state.messages.append({"role": "assistant", "content": response_text})

elif menu == "Browse All Topics":
    st.title("📚 Python Curriculum & Knowledge Base")
    st.markdown("Explore structured code topics:")

    for topic_key, topic_data in PYTHON_KNOWLEDGE_BASE.items():
        with st.expander(f"🔹 {topic_data['title']} — [{topic_data['category']}]"):
            st.write(topic_data['explanation'])
            st.code(topic_data['code'], language="python")

elif menu == "Project Info":
    st.title("ℹ️ PyGuide AI — Project Details")
    st.markdown("""
    ### 🚀 DecodeLab AI Internship Project
    Created by **Farhan**. Built with Streamlit and Python.
    """)