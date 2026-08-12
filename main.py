"""
PyGuide AI - CLI Version
A conversational AI chatbot for learning Python concepts

Author: Farhan (DecodeLab Internship)
Version: 1.0.0
"""

import json
import os
from typing import Dict, Optional, Any


def load_knowledge_base(filepath: str = "intents.json") -> Dict[str, Any]:
    """
    Load the knowledge base from a JSON file.
    
    Args:
        filepath (str): Path to the intents.json file
        
    Returns:
        Dict[str, Any]: Knowledge base dictionary with topics and their details
    """
    if not os.path.exists(filepath):
        print(f"❌ Error: {filepath} file not found!")
        return {}
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"❌ Error: {filepath} is not a valid JSON file!")
        return {}


def display_dashboard() -> None:
    """
    Display the professional CLI dashboard header.
    Clears screen and shows welcome message with available commands.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 70)
    print(" " * 10 + "🚀  PyGuide AI: Smart Learning Engine")
    print(" " * 15 + "Learn Python Concepts with AI 🐍")
    print("=" * 70)
    print()
    print(" Welcome! I am your intelligent Python tutor.")
    print(" Ask me about any Python concept and I'll explain it with examples!")
    print()
    print(" Available Commands:")
    print("   • 'menu'   - View all available topics")
    print("   • 'clear'  - Clear screen and refresh")
    print("   • 'exit'   - Exit the chatbot")
    print("-" * 70)


def display_topic_menu(kb: Dict[str, Any]) -> None:
    """
    Display all available topics from the knowledge base.
    
    Args:
        kb (Dict[str, Any]): Knowledge base dictionary
    """
    if not kb:
        print("\n❌ No topics available in the knowledge base!")
        return
        
    print("\n" + "=" * 50)
    print("📚 Available Python Learning Topics:")
    print("=" * 50)
    for index, topic in enumerate(kb.keys(), 1):
        print(f"  {index:2d}. {topic.title()}")
    print("=" * 50)
    print(f"\n💡 Total topics available: {len(kb)}")
    print("   Type a topic name to learn about it!")
    print("-" * 50)


def find_matching_topic(user_input: str, knowledge_base: Dict[str, Any]) -> Optional[str]:
    """
    Find a matching topic from the knowledge base using fuzzy matching.
    
    Args:
        user_input (str): User's input text
        knowledge_base (Dict[str, Any]): Knowledge base dictionary
        
    Returns:
        Optional[str]: Matched topic name or None
    """
    # Direct match (case-insensitive)
    if user_input in knowledge_base:
        return user_input
    
    # Substring matching for multi-word topics
    for topic in knowledge_base:
        if topic in user_input:
            return topic
    
    # Partial word matching
    words = user_input.split()
    for word in words:
        for topic in knowledge_base:
            if word in topic.split():
                return topic
    
    return None


def display_topic_response(topic: str, data: Dict[str, Any]) -> None:
    """
    Display detailed information about a Python topic.
    
    Args:
        topic (str): Topic name
        data (Dict[str, Any]): Topic data containing definition, example, and syntax
    """
    print("\n" + "=" * 70)
    print(f"📌 TOPIC: {topic.upper()}")
    print("=" * 70)
    print(f"\n📖 Definition:")
    print(f"   {data.get('definition', 'No definition available')}")
    print(f"\n💡 Real-Life Example:")
    print(f"   {data.get('example', 'No example available')}")
    print(f"\n💻 Code Syntax:")
    for line in data.get('syntax', '').split('\n'):
        print(f"   {line}")
    print("\n" + "-" * 70)


def run_chatbot() -> None:
    """
    Main chatbot loop that handles user interactions.
    Processes commands and questions, providing responses from the knowledge base.
    """
    knowledge_base = load_knowledge_base()
    
    if not knowledge_base:
        print("❌ Failed to load knowledge base. Exiting...")
        return
    
    display_dashboard()
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip().lower()
            
            # Sanitization check - ignore empty input
            if not user_input:
                continue
            
            # Handle system commands
            if user_input in ["exit", "quit", "bye"]:
                print("\n" + "=" * 70)
                print("🤖 PyGuide AI: Thank you for learning with me! 🎓")
                print("   Keep coding, keep growing! Happy Python journey 🐍✨")
                print("=" * 70 + "\n")
                break
                
            elif user_input == "clear":
                display_dashboard()
                continue
                
            elif user_input in ["menu", "topics", "help"]:
                display_topic_menu(knowledge_base)
                continue
            
            # Find and display matching topic
            matched_topic = find_matching_topic(user_input, knowledge_base)
            
            if matched_topic:
                data = knowledge_base[matched_topic]
                display_topic_response(matched_topic, data)
            else:
                print("\n❌ Topic not found!")
                print("   Let me suggest: Type 'menu' to see all available Python topics.")
                print("   Or ask me about concepts like: variable, function, loop, class, etc.")
                
        except KeyboardInterrupt:
            print("\n\n🤖 PyGuide AI: Shutting down... Good luck with your coding journey!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("   Please try again or type 'menu' for available topics.")


if __name__ == "__main__":
    run_chatbot()
