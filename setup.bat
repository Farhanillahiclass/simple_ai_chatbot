@echo off
REM Quick Setup Script for PyGuide AI on Windows

echo.
echo ========================================
echo PyGuide AI - Quick Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    exit /b 1
)

echo [1/4] Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo [2/4] Upgrading pip...
python -m pip install --upgrade pip

echo [3/4] Installing dependencies...
pip install -r requirements.txt

echo [4/4] Setup complete!
echo.
echo ========================================
echo To run the application:
echo.
echo For Web Interface (Streamlit):
echo   streamlit run app.py
echo.
echo For CLI Interface:
echo   python main.py
echo ========================================
echo.
pause
