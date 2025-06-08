@echo off
echo Starting GitHub Guide Full Stack Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo Installing dependencies...
cd backend
pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies (this may take a minute)...
    pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart pydantic[email]
)

REM Start the backend server
echo.
echo Starting FastAPI backend server...
echo Backend will be available at: http://localhost:8000
echo API documentation at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.
start cmd /k "cd backend && python main.py"

REM Wait a moment for server to start
timeout /t 3 /nobreak >nul

REM Open the frontend in default browser
echo Opening frontend in browser...
cd ..
start index.html

echo.
echo ===================================
echo GitHub Guide is now running!
echo ===================================
echo Backend: http://localhost:8000
echo Frontend: Open index.html in browser
echo.
echo To stop: Press Ctrl+C in the backend window
echo.
pause