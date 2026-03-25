@echo off
REM Run Django dev server on port 11000
REM Usage: Open Command Prompt, cd to 'city' folder and run: runserver.bat
SET PORT=11000
python manage.py runserver 0.0.0.0:%PORT%
