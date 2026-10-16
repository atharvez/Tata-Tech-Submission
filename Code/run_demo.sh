#!/usr/bin/env bash
# Master demonstration script for AUTOSAR-AI
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "======================================================================"
echo "  AUTOSAR-AI: CAPSTONE DEMONSTRATION LAUNCHER"
echo "  Candidate: Atharva Desai (PRN: 123B1D059) | PCCOE AIML"
echo "======================================================================"

echo "[1/2] Running automated architectural benchmark suite..."
python3 run_evaluation.py

echo "[2/2] Launching Web UI server on port 8081..."
echo "Open your browser to: http://localhost:8081"
python3 app_web_gui.py 8081
