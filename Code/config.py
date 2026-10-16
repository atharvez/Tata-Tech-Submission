"""
AUTOSAR-AI Configuration Module
Defines absolute and relative paths, retrieval hyperparameters, and model configurations.
"""

import os
from pathlib import Path

# Base Directory Paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DATA_DIR = BASE_DIR / "Input_Data"
RAW_DOCS_DIR = INPUT_DATA_DIR / "raw_documents"
ARXML_DIR = INPUT_DATA_DIR / "arxml_catalogs"
GROUND_TRUTH_DIR = INPUT_DATA_DIR / "ground_truth"
EVALUATION_DIR = BASE_DIR / "Evaluation_Results"
PROMPTS_CONFIG_DIR = BASE_DIR / "Model_Prompts_Config"
DOCUMENTATION_DIR = BASE_DIR / "Documentation"

# Knowledge Base PDF Files
PDF_FILES = [
    RAW_DOCS_DIR / "AUTOSAR_HLD_BCM_BodyControlModule_v2.4.pdf",
    RAW_DOCS_DIR / "AUTOSAR_HLD_BCM_v2.3_Legacy_Comparison.pdf",
    RAW_DOCS_DIR / "AUTOSAR_HLD_ADAS_DomainController_v1.2.pdf",
    RAW_DOCS_DIR / "AUTOSAR_HLD_BMS_BatteryManagementSystem_v3.1.pdf",
]

# ARXML Files
ARXML_FILES = [
    ARXML_DIR / "bcm_components.arxml",
    ARXML_DIR / "adas_components.arxml",
]

# Retrieval Hyperparameters
BM25_ALPHA = 0.45       # Weight for keyword matching
DENSE_BETA = 0.55       # Weight for semantic cosine similarity
DEFAULT_TOP_K = 3       # Top passages retrieved for context
MIN_SIMILARITY_SCORE = 0.15

# Model Settings
LLM_PROVIDER = "Google Gemini / Fallback Deterministic Grounded Engine"
PRIMARY_MODEL = "gemini-1.5-pro"
FALLBACK_MODEL = "gemini-1.5-flash"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TEMPERATURE = 0.1
MAX_OUTPUT_TOKENS = 1500

# Evaluation Benchmarks
GROUND_TRUTH_BENCHMARK_FILE = EVALUATION_DIR / "test_ground_truth_qa_pairs.json"
EVAL_REPORT_OUTPUT = EVALUATION_DIR / "evaluation_report.json"
EVAL_SUMMARY_OUTPUT = EVALUATION_DIR / "evaluation_metrics_summary.md"
