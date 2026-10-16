# PCCOE CS-AIML & TATA TECHNOLOGIES CAPSTONE PROJECT

## AUTOSAR HLD Document Analysis Assistant Using Grounded RAG & Deterministic Architecture Verification

**Candidate:** Atharva Desai  
**PRN:** 123B1D059 | **Roll No:** 123B1D059  
**Class:** Final Year B.Tech Computer Engineering (AI & ML)  
**Institution:** Pimpri Chinchwad College of Engineering (PCCOE), Pune  
**Project Guide:** Prof. Dr. S. K. Kulkarni  
**Industry Reference:** Tata Technologies Reference Solution (Case Study 1: AUTOSAR HLD Analysis Assistant)  
**Evaluation Rubric:** 100-Mark Applied AI/ML Project Rubric  

---

## 📁 Submission Folder Structure

```
PCCOE_Atharva_PRN_123B1D059_AUTOSAR_AI/
├── Synopsis/
│   ├── Project_Synopsis.md               # Approved synopsis & technical plan
│   ├── Project_Synopsis_AUTOSAR_AI.pdf   # Formally formatted PDF synopsis
│   ├── generate_synopsis_pdf.py          # PDF generation script
│   └── Faculty_Approval_Record.md        # Continuous evaluation review sheet
├── Declarations/
│   ├── Student_Declaration.md            # Formally signed student declaration
│   ├── Faculty_Approval_Signature_Form.md# Faculty & institutional approval certificate
│   └── Plagiarism_Free_Certificate.md    # Originality & AI compliance certificate
├── Input_Data/
│   ├── raw_documents/                    # Multi-page HLD technical specification PDFs
│   │   ├── AUTOSAR_HLD_BCM_BodyControlModule_v2.4.pdf
│   │   ├── AUTOSAR_HLD_BCM_v2.3_Legacy_Comparison.pdf
│   │   ├── AUTOSAR_HLD_ADAS_DomainController_v1.2.pdf
│   │   └── AUTOSAR_HLD_BMS_BatteryManagementSystem_v3.1.pdf
│   ├── arxml_catalogs/                   # AUTOSAR 4.4 ARXML component models
│   │   ├── bcm_components.arxml
│   │   └── adas_components.arxml
│   ├── ground_truth/                     # Annotated ground truth definitions
│   │   ├── bcm_swc_ground_truth.json
│   │   └── inconsistency_ground_truth.json
│   └── knowledge_base_metadata.json      # Provenance and corpus metadata
├── Model_Prompts_Config/
│   ├── system_prompts.json               # Specialized role system prompts
│   ├── prompt_templates.md               # Few-shot, CoT & citation templates
│   ├── model_config.yaml                 # Retrieval & LLM configuration
│   ├── vector_store_config.json          # Index parameters & distance metrics
│   └── tools_definition.json             # Function calling tool signatures
├── Code/
│   ├── parsers/                          # Document & model extractors
│   │   ├── pdf_parser.py                 # PyPDF technical document parser
│   │   └── arxml_parser.py               # XML component model parser
│   ├── config.py                         # Unified paths & hyperparameters
│   ├── vector_store.py                   # Self-contained dense vector index
│   ├── retriever.py                      # Hybrid BM25 + Dense Cosine search
│   ├── rag_pipeline.py                   # Grounded RAG & citation generator
│   ├── autosar_analyzer.py               # Deterministic VFB consistency & diff engine
│   ├── evaluation_metrics.py             # RAGAS metric implementations
│   ├── run_evaluation.py                 # Automated benchmark test suite
│   ├── app_web_gui.py                    # Lightweight Web UI server (Port 8081)
│   ├── cli_interactive.py                # Terminal architectural consultation CLI
│   ├── run_evaluation.bat                # Windows 1-click evaluation launcher
│   ├── run_cli.bat                       # Windows 1-click CLI launcher
│   ├── run_web_gui.bat                   # Windows 1-click Web GUI launcher
│   ├── requirements.txt                  # Python dependencies
│   └── run_demo.sh                       # Linux/macOS demonstration script
├── Evaluation_Results/
│   ├── test_ground_truth_qa_pairs.json   # 15 Ground-truth test scenarios
│   ├── evaluation_report.json            # Machine-readable benchmark results
│   ├── evaluation_metrics_summary.md     # Markdown metrics summary table
│   └── sample_grounded_responses_with_citations.md # Verified output evidence
├── Documentation/
│   ├── Technical_Report_PCCOE_AIML.md    # Full academic & technical report
│   ├── Architecture_Diagram.md           # Mermaid system & sequence diagrams
│   ├── User_Manual_and_Setup_Guide.md    # Setup & operation manual
│   └── 100_Mark_Rubric_Self_Assessment.md# Detailed rubric compliance mapping
├── Video/
│   ├── Demonstration_Script_and_Storyboard.md # 8-minute presentation script
│   ├── Presentation_Slides_Outline.md    # 12-slide defense presentation deck
│   └── Video_Recording_Checklist.md      # Recording guidelines & technical checklist
├── README.md                             # Project overview & navigation guide
└── .gitignore                            # Clean repository filter
```

---

## 🚀 How to Run the Project

Navigate to the `Code/` folder:

```powershell
# 1. Run Automated Evaluation Benchmark (15 Test Cases):
python run_evaluation.py
# Or double-click run_evaluation.bat

# 2. Launch Interactive Terminal Console:
python cli_interactive.py
# Or double-click run_cli.bat

# 3. Launch Modern Web UI & API Server (Port 8081):
python app_web_gui.py 8081
# Or double-click run_web_gui.bat
```
