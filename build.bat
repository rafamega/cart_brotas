@echo off
rd /s /q dist
rd /s /q build
del main.spec
pyinstaller --console --onefile --icon=python.ico main.py
pause
