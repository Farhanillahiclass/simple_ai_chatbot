#!/bin/bash

# Quick Setup Script for PyGuide AI on macOS/Linux

echo ""
echo "========================================"
echo "PyGuide AI - Quick Setup Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

echo "[1/4] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "[2/4] Upgrading pip..."
python3 -m pip install --upgrade pip

echo "[3/4] Installing dependencies..."
pip install -r requirements.txt

echo "[4/4] Setup complete!"
echo ""
echo "========================================"
echo "To run the application:"
echo ""
echo "For Web Interface (Streamlit):"
echo "   streamlit run app.py"
echo ""
echo "For CLI Interface:"
echo "   python main.py"
echo "========================================"
echo ""
