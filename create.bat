@echo off

:: Creating folders
mkdir app
mkdir app\routers
mkdir app\models
mkdir app\schemas

:: Creating files
type NUL > app\__init__.py

type NUL > app\routers\__init__.py
type NUL > app\models\__init__.py
type NUL > app\schemas\__init__.py
type NUL > requirements.txt
type NUL > README.md

echo.

echo app\
echo ├─ main.py
echo ├─ routers\
echo ├─ models\
echo ├─ schemas\
echo requirements.txt
echo README.md
echo.
pause
