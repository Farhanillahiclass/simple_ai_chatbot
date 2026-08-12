@echo off
REM ============================================================
REM PyGuide AI - GitHub Upload Script
REM ============================================================
REM This script uploads your project to GitHub
REM ============================================================

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo       PyGuide AI - GitHub Upload Script
echo ============================================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo.
    echo Please install Git from: https://git-scm.com/download/win
    echo.
    echo After installation, restart your terminal and run this script again.
    pause
    exit /b 1
)

echo [DONE] Git is installed and ready!
echo.

REM Check if we're in the right directory
if not exist "intents.json" (
    echo ERROR: This script must be run from the project_01 directory!
    echo Current directory: %cd%
    pause
    exit /b 1
)

echo [✓] Project files found!
echo.

REM Initialize git
echo [1/7] Initializing Git repository...
git init
echo [✓] Git initialized!
echo.

REM Configure git (if not already configured)
echo [2/7] Checking Git configuration...
git config user.email >nul 2>&1
if errorlevel 1 (
    echo Please enter your Git configuration:
    set /p git_name="Enter your name: "
    set /p git_email="Enter your email: "
    git config --global user.name "!git_name!"
    git config --global user.email "!git_email!"
    echo [✓] Git configured!
) else (
    echo [✓] Git already configured!
)
echo.

REM Add all files
echo [3/7] Adding all files to Git...
git add .
echo [✓] Files added!
echo.

REM Create initial commit
echo [4/7] Creating initial commit...
git commit -m "Initial commit: PyGuide AI - Smart Python Learning Chatbot"
echo [✓] Commit created!
echo.

REM Add remote repository
echo [5/7] Adding remote repository...
echo.
echo Your repository URL: https://github.com/Farhanillahiclass/simple_ai_chatbot.git
echo.
git remote add origin https://github.com/Farhanillahiclass/simple_ai_chatbot.git
echo [✓] Remote added!
echo.

REM Set branch name to main
echo [6/7] Setting branch name to main...
git branch -M main
echo [✓] Branch renamed!
echo.

REM Push to GitHub
echo [7/7] Pushing to GitHub...
echo.
echo You may be prompted for GitHub credentials:
echo  - Username: Your GitHub username
echo  - Password: Your Personal Access Token (NOT your password)
echo.
echo Need a Personal Access Token?
echo 1. Go to: https://github.com/settings/tokens
echo 2. Click "Generate new token"
echo 3. Select scope: repo
echo 4. Copy the token
echo 5. Paste it as password below
echo.
pause

git push -u origin main

echo.
echo ============================================================
echo              ✓ UPLOAD COMPLETE!
echo ============================================================
echo.
echo Your project is now on GitHub!
echo Visit: https://github.com/Farhanillahiclass/simple_ai_chatbot
echo.
echo Next steps:
echo 1. Check your repository on GitHub
echo 2. Share the link with friends
echo 3. Add to your portfolio
echo 4. Continue improving the project!
echo.
echo Happy coding! 🐍✨
echo.
pause
