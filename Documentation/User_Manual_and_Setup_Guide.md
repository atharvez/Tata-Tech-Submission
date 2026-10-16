# USER MANUAL & SETUP GUIDE

## 1. System Requirements
- **Operating System:** Windows 10/11, Ubuntu Linux 20.04+, or macOS
- **Python Version:** Python 3.10, 3.11, or 3.12
- **Hardware:** Minimum 4 GB RAM, 2 GHz dual-core CPU, 500 MB free disk space

---

## 2. Quick Setup & Launch

### Windows (1-Click Launchers):
1. Navigate to the `Code/` folder.
2. Double-click [`run_web_gui.bat`](file:///C:/Users/7atha/Downloads/PCCOE_Atharva_PRN_123B1D059_AUTOSAR_AI/Code/run_web_gui.bat) to launch the Web Interface (opens automatically at [http://localhost:8081](http://localhost:8081)).
3. Double-click [`run_cli.bat`](file:///C:/Users/7atha/Downloads/PCCOE_Atharva_PRN_123B1D059_AUTOSAR_AI/Code/run_cli.bat) to launch the interactive terminal console.
4. Double-click [`run_evaluation.bat`](file:///C:/Users/7atha/Downloads/PCCOE_Atharva_PRN_123B1D059_AUTOSAR_AI/Code/run_evaluation.bat) to run the 15-scenario benchmark test suite.

### Command Line / Linux / macOS:
```bash
# Navigate to the Code directory
cd Code

# Run Benchmark Evaluation
python3 run_evaluation.py

# Launch Interactive CLI
python3 cli_interactive.py

# Launch Web Server on Port 8081
python3 app_web_gui.py 8081
```

---

## 3. Web UI Features & Navigation
- **Semantic HLD Query Assistant:** Type inquiries regarding software components, runnables, ports, interfaces, or target silicon to receive strictly grounded responses with section and page citations.
- **VFB Inconsistency Auditor:** View real-time anomaly detection identifying dangling ports lacking providers and datatype mismatches (e.g., uint8 vs. uint16).
- **Revision Diff (v2.3 to v2.4):** Compare successive HLD releases to detect deprecated components, newly added ports, and safety rating upgrades.
- **RAGAS Benchmark Metrics:** Live card displaying Grounded Faithfulness, Relevancy, Context Precision, Citation Accuracy, and query execution latency.
