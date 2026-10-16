@echo off
echo ======================================================================
echo   Running AUTOSAR-AI Benchmark Evaluation Suite (PCCOE AIML)
echo ======================================================================
cd /d "%~dp0"
python run_evaluation.py
pause
