@echo off
set VENV_DIR=.venv
set REQUIREMENTS=requirements.txt
set GUI_DIR=GUI/src
set ROOT_DIR=%cd%
set CLI_DIR=src
set SCRIPTS_DIR=scripts

:menu
echo ================================================
echo       Python + Electron/Svelte CLI Menu Tool - Choose an option 🚀✨
echo ================================================
echo  [1] 🔨 Install Python and Node Dependencies
echo  [2] 📌 Create Desktop Shortcuts
echo  [3] 🖥️  Open CLI Menu
echo  [4] 🐍 Run Python + 🌶️  Flask Backend
echo  [5] ⚛️  Run Electron + 🔥 Svelte GUI
echo  [6] 🔄 Run All
echo  [7] 🧹 Clean Environment
echo  [0] 🚪 Exit
echo  [venv] 🐍 Activate Virtual Environment
echo ================================================
set /p choice="Enter your choice (0-8, venv): "

if "%choice%"=="1" goto install
if "%choice%"=="2" goto create_shortcuts
if "%choice%"=="3" goto open_CLI_Menu 
if "%choice%"=="4" goto run_flask_backend
if "%choice%"=="5" goto run_GUI
if "%choice%"=="6" goto run_All
if "%choice%"=="venv" goto activate_venv exit :eof
if "%choice%"=="7" goto clean
if "%choice%"=="0" goto exit :eof

echo Invalid choice. Please select a valid option.
goto menu

:install
echo ================================================
echo Installing Python and Node.js dependencies...
echo ================================================
if not exist %VENV_DIR%\Scripts\python.exe (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
) else (
    echo Virtual environment already exists.
)

echo Installing Python dependencies...
%VENV_DIR%\Scripts\python.exe -m pip install --upgrade pip
%VENV_DIR%\Scripts\python.exe -m pip install -r %REQUIREMENTS%

echo Installing Node.js dependencies...
cd %GUI_DIR%
call npm install
call npm audit fix
cd %ROOT_DIR%
echo ================================================
echo Installation complete!
echo ================================================
pause
goto menu

:open_CLI_Menu
echo ================================================
echo Opening the CLI menu...
echo ================================================
rem # Runs the CLI tasks in the current terminal
start cmd /k "%VENV_DIR%\Scripts\python.exe %CLI_DIR%/run.py --help && %VENV_DIR%\Scripts\python.exe %CLI_DIR%/run.py show-menu" 
pause
goto menu

:run_flask_backend
echo ================================================
echo Starting the flask backend...
echo ================================================
rem # Starts the backend in a new terminal using a CLI task
start cmd /k "%VENV_DIR%\Scripts\python.exe %CLI_DIR%/run.py --help && %VENV_DIR%\Scripts\python.exe %CLI_DIR%/run.py run-backend" 
pause
goto menu

:run_GUI
echo ================================================
echo Starting the Electron + Svelte GUI...
echo ================================================
cd %GUI_DIR%
rem # Starts the Electron GUI in a new terminal
start npm run dev
cd %ROOT_DIR%
pause
goto menu

:run_All
echo ================================================
echo Running all components...
echo ================================================
start cmd /k "%VENV_DIR%\Scripts\python.exe %CLI_DIR%/run.py run-backend"
start cmd /k "cd %GUI_DIR% && npm run dev"
pause
goto menu

:create_shortcuts
echo ================================================
echo Creating shortcuts...
echo ================================================
%VENV_DIR%\Scripts\python.exe %SCRIPTS_DIR%/create_shortcuts.py
pause
goto menu

:activate_venv
echo ================================================
echo Activating the virtual environment...
echo ================================================
call %VENV_DIR%\Scripts\activate.bat
echo Virtual environment activated!
echo ================================================
goto menu

:clean
echo ================================================
echo Cleaning up the environment...
echo ================================================
echo Removing virtual environment...
rmdir /S /Q %VENV_DIR%
echo Removing shortcuts...
del shortcuts\*.lnk
pause
goto menu

:exit
echo Exiting the Spike Tool script... See you soon! 👋
%VENV_DIR%\Scripts\python.exe %CLI_DIR%/run.py --help
REM Activate the virtual environment
call %VENV_DIR%\Scripts\activate.bat
