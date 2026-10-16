@echo off
echo ======================================================================
echo   Launching AUTOSAR-AI Web UI & API Server (PCCOE AIML / TTL)
echo ======================================================================
cd /d "%~dp0"
echo Starting web server on http://localhost:8081 ...
start http://localhost:8081
python app_web_gui.py 8081
pause
