# Contributing to PyGuide AI

First off, thank you for considering contributing to PyGuide AI! It's people like you that make PyGuide AI such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Explain why this enhancement would be useful**

### Pull Requests

- Fill in the required template
- Follow the Python PEP 8 style guide
- Include appropriate test cases
- End all files with a newline
- Avoid platform-dependent code
- Document new code based on the existing documentation style

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Running Tests

Before submitting a pull request, test your changes:

```bash
# Test CLI version
python main.py

# Test Web version (if Streamlit is installed)
streamlit run app.py
```

## Style Guide

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for all functions
- Include docstrings for all functions and classes
- Keep lines under 100 characters when possible
- Use meaningful variable names

### Example Function:

```python
def find_matching_topic(user_input: str, knowledge_base: Dict[str, Any]) -> Optional[tuple]:
    """
    Find a matching topic from the knowledge base.
    
    Args:
        user_input (str): User's query text
        knowledge_base (Dict[str, Any]): Knowledge base dictionary
        
    Returns:
        Optional[tuple]: (topic_name, topic_data) if found, None otherwise
    """
    # Implementation here
    pass
```

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line
- Examples:
  - `Add: Support for decorators topic`
  - `Fix: Improve topic matching algorithm`
  - `Update: Enhance Streamlit UI with better styling`
  - `Docs: Update README with new features`

## Adding New Topics

To add new Python topics to the knowledge base:

1. Edit `intents.json`
2. Add a new topic entry with the following structure:
   ```json
   {
       "topic_name": {
           "definition": "Clear, concise definition",
           "example": "Real-life analogy with emojis",
           "syntax": "Practical code example",
           "keywords": ["alternative", "search", "terms"]
       }
   }
   ```
3. Ensure the JSON is valid
4. Test with both CLI and web interfaces
5. Submit a pull request with the new topics

### Guidelines for New Topics:

- ✅ Use clear, beginner-friendly language
- ✅ Include at least one emoji in the example
- ✅ Provide practical code examples
- ✅ Keep definitions concise (1-2 sentences)
- ✅ Add relevant keywords for search functionality
- ✅ Test the topic with the matching algorithm

## Improving Existing Topics

To improve existing topics:

1. Identify areas that need enhancement
2. Make your improvements following the guidelines above
3. Test the changes
4. Submit a pull request with a clear description of improvements

## Documentation

- Use clear, concise language
- Include examples where appropriate
- Keep documentation up-to-date with code changes
- Follow Markdown formatting standards

## Additional Notes

### Issue and Pull Request Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed

## Recognition

Contributors will be recognized in the README.md file under the "Contributors" section.

---

Thank you for contributing to PyGuide AI! 🎉
