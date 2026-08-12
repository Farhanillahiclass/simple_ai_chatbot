# 🐍 PyGuide AI: Smart Python Learning Engine

[![Python Version](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)

> **An intelligent AI-powered chatbot designed to help beginners learn Python concepts through interactive explanations, real-life examples, and code snippets.**

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [🎯 Project Overview](#-project-overview)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [📚 Available Topics](#-available-topics)
- [🏗️ Project Structure](#️-project-structure)
- [💡 How It Works](#-how-it-works)
- [🎨 User Interface](#-user-interface)
- [🔧 Technologies Used](#-technologies-used)
- [📝 Learning Journey](#-learning-journey)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)
- [🙏 Acknowledgments](#-acknowledgments)

---

## ✨ Features

### 🎓 Comprehensive Learning Content
- **20+ Python Topics** covering basics to advanced concepts
- Each topic includes:
  - 📖 Clear, beginner-friendly definitions
  - 💡 Real-life analogies and examples
  - 💻 Practical code snippets ready to run
  - 🎯 Relevant keywords for better search

### 🖥️ Dual Interface
- **Web Interface (Streamlit)**: Modern, interactive UI with chat history
- **CLI Interface**: Fast, lightweight command-line access

### 🤖 Smart Topic Matching
- Direct topic matching (case-insensitive)
- Intelligent substring matching
- Fuzzy keyword recognition
- Helpful error messages with suggestions

### 📱 User-Friendly Design
- Clean, professional interface
- Topic explorer sidebar (Web version)
- Chat history preservation
- Responsive and accessible design

### 🎯 Topics Covered
- Variables & Data Types
- Collections (List, Tuple, Dictionary, Set)
- Control Flow (If statements, Loops)
- Functions & Advanced Functions
- Object-Oriented Programming (OOP)
- Exception Handling
- File I/O & JSON
- List Comprehensions & Generators
- Decorators & Modules
- String Methods & Operations

---

## 🎯 Project Overview

**PyGuide AI** is my first project in the **DecodeLab AI Internship Program**. It demonstrates:
- ✅ Python fundamentals and best practices
- ✅ Clean code with type hints and documentation
- ✅ Interactive application development
- ✅ Knowledge base management with JSON
- ✅ User interface design (CLI & Web)
- ✅ Professional software development practices

This project showcases practical skills in building educational tools using Python.

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.7 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package manager, usually comes with Python)
- **Git** (for cloning the repository)

### Installation

#### Step 1: Clone the Repository
```bash
git clone https://github.com/Farhanillahiclass/simple_ai_chatbot.git
cd simple_ai_chatbot/project_01
```

#### Step 2: Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Running the Application

#### Option 1: Web Interface (Streamlit) - Recommended 🌐
```bash
streamlit run app.py
```
This will open the interactive web interface in your default browser at `http://localhost:8501`

#### Option 2: Command-Line Interface (CLI) 🖥️
```bash
python main.py
```

#### Step 4: Start Learning!
- For Web: Type your Python question in the chat box
- For CLI: Type a Python topic and press Enter
- Type `menu` (CLI) to see all available topics
- Type `exit` to quit the application

---

## 📚 Available Topics

The knowledge base includes learning materials for:

### Fundamentals
- **Variables** - Understanding data containers
- **Data Types** - int, float, str, bool, and more
- **Strings** - Text manipulation and operations
- **Slicing** - Extracting portions of sequences

### Collections
- **List** - Ordered, mutable collections
- **Tuple** - Immutable sequences
- **Dictionary** - Key-value data structure
- **Set** - Unique, unordered elements

### Control Flow
- **If Statement** - Conditional execution
- **Loop** - Repetition with for and while

### Functions & Methods
- **Function** - Reusable code blocks
- **Lambda** - Anonymous functions
- **List Methods** - append(), remove(), sort(), etc.
- **String Methods** - upper(), lower(), replace(), etc.
- **List Comprehension** - Concise list creation

### Advanced Topics
- **Exception Handling** - Try-except blocks
- **Class** - Object-oriented programming basics
- **Decorator** - Function modification and enhancement
- **Generator** - Memory-efficient iterations
- **Module** - Code organization and reuse
- **File Handling** - Reading and writing files
- **JSON** - Data serialization format
- **OOP Principles** - Inheritance, polymorphism, encapsulation
- **Map Filter Reduce** - Functional programming concepts

---

## 🏗️ Project Structure

```
simple_ai_chatbot/
└── project_01/
    ├── app.py                 # 🌐 Streamlit web interface
    ├── main.py                # 🖥️  CLI chatbot application
    ├── intents.json           # 📚 Knowledge base with Python topics
    ├── requirements.txt       # 📦 Python dependencies
    ├── .gitignore            # 🚫 Git ignore rules
    ├── LICENSE               # 📜 MIT License
    ├── README.md             # 📖 This file
    └── .venv/                # 🔧 Virtual environment (created locally)
```

### File Descriptions

| File | Purpose |
|------|---------|
| **app.py** | Streamlit web application with modern UI and chat interface |
| **main.py** | CLI version with professional terminal interface |
| **intents.json** | JSON knowledge base containing all Python topics and explanations |
| **requirements.txt** | Lists all Python package dependencies |
| **.gitignore** | Specifies which files Git should ignore |
| **LICENSE** | MIT License for the project |

---

## 💡 How It Works

### Architecture Overview

```
User Input
    ↓
Input Validation & Sanitization
    ↓
Topic Matching Algorithm
    ├─ Direct Match (case-insensitive)
    ├─ Substring Matching
    └─ Keyword Matching
    ↓
Knowledge Base Lookup
    ↓
Response Formatting
    ├─ Definition
    ├─ Real-life Example
    └─ Code Syntax
    ↓
Display Output
```

### Matching Algorithm

The chatbot uses a multi-level matching strategy:

1. **Direct Match**: Checks if user input exactly matches a topic
2. **Substring Matching**: Looks for topics within the user's query
3. **Keyword Matching**: Searches for keywords related to topics
4. **Fallback**: Suggests available topics if no match is found

### Knowledge Base Format

Each topic in `intents.json` contains:
```json
{
    "topic_name": {
        "definition": "Clear explanation of the concept",
        "example": "Real-life analogy with emojis",
        "syntax": "Code example showing usage",
        "keywords": ["alternative", "names", "for", "searching"]
    }
}
```

---

## 🎨 User Interface

### Web Interface (Streamlit)
- Modern, responsive chat interface
- Topics explorer sidebar
- Real-time chat history
- Code syntax highlighting
- Professional styling with custom CSS
- Mobile-friendly design

### CLI Interface
- Professional ASCII dashboard
- Color-coded messages with emojis
- Clean topic display
- Help menu with available commands
- Error handling with suggestions

---

## 🔧 Technologies Used

### Core Technologies
- **Python 3.7+** - Primary programming language
- **Streamlit** - Web application framework
- **JSON** - Data format for knowledge base

### Development Practices
- Type hints for better code quality
- Comprehensive docstrings
- Professional error handling
- Modular function design
- UTF-8 encoding support

### Tools & Libraries
- **Standard Library**: json, os, typing

---

## 📝 Learning Journey

This project demonstrates the following programming concepts:

✅ **Python Basics**
- Variables and data types
- String manipulation
- List and dictionary operations

✅ **Object-Oriented Programming**
- Functions with type hints
- Proper documentation
- Clean code principles

✅ **File I/O & Data Handling**
- JSON file parsing
- Error handling
- UTF-8 encoding

✅ **User Interface Development**
- CLI design
- Web application with Streamlit
- User experience considerations

✅ **Software Engineering**
- Project structure
- Version control ready
- Professional documentation

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

1. **Add More Topics**
   - Expand the knowledge base with new Python concepts
   - Include diverse real-life examples
   - Provide clear, beginner-friendly explanations

2. **Improve Existing Content**
   - Refine explanations
   - Add more code examples
   - Fix typos or inaccuracies

3. **Enhance Features**
   - Improve the matching algorithm
   - Add new UI features
   - Optimize performance

4. **Report Issues**
   - Find and report bugs
   - Suggest improvements
   - Provide feedback on usability

### Steps to Contribute

1. **Fork the Repository**
   ```bash
   Click the "Fork" button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/simple_ai_chatbot.git
   cd simple_ai_chatbot/project_01
   ```

3. **Create a New Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Edit files
   - Test your changes
   - Ensure code quality

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of changes"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to GitHub and create a PR
   - Provide a clear description of changes
   - Wait for review and merge

### Contribution Guidelines
- Follow Python PEP 8 style guide
- Add type hints to functions
- Include docstrings for all functions
- Test your changes before submitting
- Keep commit messages clear and descriptive

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary
You are free to:
- ✅ Use this code for personal projects
- ✅ Modify and distribute the code
- ✅ Use commercially
- ✅ Private use

You must:
- 📋 Include the license and copyright notice

---

## 👨‍💻 Author

**Farhan**
- 🎓 DecodeLab AI Internship Program
- 🐍 Python Enthusiast & Developer
- 🤖 AI/ML Learner

### Connect
- GitHub: [Farhanillahiclass](https://github.com/Farhanillahiclass)
- Repository: [simple_ai_chatbot](https://github.com/Farhanillahiclass/simple_ai_chatbot)

---

## 🙏 Acknowledgments

- **DecodeLab** - For the internship opportunity and learning platform
- **Streamlit** - For the amazing web framework
- **Python Community** - For excellent documentation and tools
- **All Contributors** - For helping improve this project

---

## 🚀 Future Enhancements

Planned features and improvements:

- [ ] Add voice input/output capability
- [ ] Implement user progress tracking
- [ ] Add quiz and assessment features
- [ ] Multi-language support
- [ ] Database backend for user profiles
- [ ] Advanced NLP for better matching
- [ ] API for integration with other apps
- [ ] Mobile app version
- [ ] Community forum for discussions
- [ ] Interactive code playground

---

## 📞 Support

Need help? Here's what you can do:

1. **Check the README** - Most common issues are covered here
2. **Review intents.json** - Understand the knowledge base structure
3. **Read the Code Comments** - Functions have detailed docstrings
4. **Open an Issue** - Report bugs or request features on GitHub

---

## 📚 Learning Resources

Want to learn more about the technologies used?

- [Python Official Documentation](https://docs.python.org/3/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [JSON Format Guide](https://www.json.org/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

---

## 📊 Project Statistics

- **Python Topics**: 20+
- **Code Examples**: 30+
- **Lines of Code**: 300+
- **Documentation**: Comprehensive
- **Test Coverage**: Ready for testing

---

## 🎉 Conclusion

PyGuide AI is designed to make learning Python fun, interactive, and accessible for beginners. Whether you're just starting your Python journey or brushing up on concepts, this chatbot is here to help!

**Happy Learning! 🐍✨**

---

<div align="center">

**Made with ❤️ during DecodeLab AI Internship**

[⭐ Star the Repository](https://github.com/Farhanillahiclass/simple_ai_chatbot) • [🐛 Report Issues](https://github.com/Farhanillahiclass/simple_ai_chatbot/issues) • [💡 Suggest Features](https://github.com/Farhanillahiclass/simple_ai_chatbot/issues)

</div>
