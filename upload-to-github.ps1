# ============================================================
# PyGuide AI - GitHub Upload Script (PowerShell Version)
# ============================================================
# This script uploads your project to GitHub
# Usage: Run from project_01 directory
# ============================================================

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "       PyGuide AI - GitHub Upload Script" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
try {
    $gitVersion = git --version
    Write-Host "[✓] Git is installed: $gitVersion" -ForegroundColor Green
}
catch {
    Write-Host "ERROR: Git is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "After installation, restart PowerShell and run this script again." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Check if we're in the right directory
if (-not (Test-Path "intents.json")) {
    Write-Host "ERROR: This script must be run from the project_01 directory!" -ForegroundColor Red
    Write-Host "Current directory: $(Get-Location)" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[✓] Project files found!" -ForegroundColor Green
Write-Host ""

# Initialize git
Write-Host "[1/7] Initializing Git repository..." -ForegroundColor Cyan
git init
Write-Host "[✓] Git initialized!" -ForegroundColor Green
Write-Host ""

# Configure git (if not already configured)
Write-Host "[2/7] Checking Git configuration..." -ForegroundColor Cyan
try {
    $gitName = git config user.name 2>&1
    if ([string]::IsNullOrEmpty($gitName) -or $gitName -like "*error*") {
        Write-Host "Please enter your Git configuration:" -ForegroundColor Yellow
        $gitName = Read-Host "Enter your name"
        $gitEmail = Read-Host "Enter your email"
        git config --global user.name $gitName
        git config --global user.email $gitEmail
        Write-Host "[✓] Git configured!" -ForegroundColor Green
    }
    else {
        Write-Host "[✓] Git already configured!" -ForegroundColor Green
    }
}
catch {
    Write-Host "Please enter your Git configuration:" -ForegroundColor Yellow
    $gitName = Read-Host "Enter your name"
    $gitEmail = Read-Host "Enter your email"
    git config --global user.name $gitName
    git config --global user.email $gitEmail
    Write-Host "[✓] Git configured!" -ForegroundColor Green
}
Write-Host ""

# Add all files
Write-Host "[3/7] Adding all files to Git..." -ForegroundColor Cyan
git add .
Write-Host "[✓] Files added!" -ForegroundColor Green
Write-Host ""

# Create initial commit
Write-Host "[4/7] Creating initial commit..." -ForegroundColor Cyan
git commit -m "Initial commit: PyGuide AI - Smart Python Learning Chatbot"
Write-Host "[✓] Commit created!" -ForegroundColor Green
Write-Host ""

# Add remote repository
Write-Host "[5/7] Adding remote repository..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Your repository URL: https://github.com/Farhanillahiclass/simple_ai_chatbot.git" -ForegroundColor Yellow
Write-Host ""
git remote add origin https://github.com/Farhanillahiclass/simple_ai_chatbot.git
Write-Host "[✓] Remote added!" -ForegroundColor Green
Write-Host ""

# Set branch name to main
Write-Host "[6/7] Setting branch name to main..." -ForegroundColor Cyan
git branch -M main
Write-Host "[✓] Branch renamed!" -ForegroundColor Green
Write-Host ""

# Push to GitHub
Write-Host "[7/7] Pushing to GitHub..." -ForegroundColor Cyan
Write-Host ""
Write-Host "You may be prompted for GitHub credentials:" -ForegroundColor Yellow
Write-Host " - Username: Your GitHub username" -ForegroundColor Yellow
Write-Host " - Password: Your Personal Access Token (NOT your password)" -ForegroundColor Yellow
Write-Host ""
Write-Host "Need a Personal Access Token?" -ForegroundColor Yellow
Write-Host "1. Go to: https://github.com/settings/tokens" -ForegroundColor Yellow
Write-Host "2. Click 'Generate new token'" -ForegroundColor Yellow
Write-Host "3. Select scope: repo" -ForegroundColor Yellow
Write-Host "4. Copy the token" -ForegroundColor Yellow
Write-Host "5. Paste it as password below" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to continue"

git push -u origin main

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "              ✓ UPLOAD COMPLETE!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Your project is now on GitHub!" -ForegroundColor Green
Write-Host "Visit: https://github.com/Farhanillahiclass/simple_ai_chatbot" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Check your repository on GitHub" -ForegroundColor Yellow
Write-Host "2. Share the link with friends" -ForegroundColor Yellow
Write-Host "3. Add to your portfolio" -ForegroundColor Yellow
Write-Host "4. Continue improving the project!" -ForegroundColor Yellow
Write-Host ""
Write-Host "Happy coding! 🐍✨" -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to exit"
