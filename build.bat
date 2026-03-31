@echo off
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies.
    pause
    exit /b %errorlevel%
)

echo Installing PyInstaller...
pip install pyinstaller
if %errorlevel% neq 0 (
    echo Error installing PyInstaller.
    pause
    exit /b %errorlevel%
)

echo Building the executable...
pyinstaller --clean build_windows.spec
if %errorlevel% neq 0 (
    echo Error building the executable.
    pause
    exit /b %errorlevel%
)

echo Build successful! The executable can be found in the dist/ folder.
pause
