# 100-MARK APPLIED AI/ML RUBRIC COMPLIANCE & SELF-ASSESSMENT

**Candidate Name:** Atharva Desai  
**PRN:** 123B1D059  
**Roll No:** 123B1D059  
**Institution:** Pimpri Chinchwad College of Engineering (PCCOE), Pune  
**Project:** AUTOSAR HLD Document Analysis Assistant (Tata Technologies Reference Solution Case Study 1)  

---

| Rubric Component | Max Marks | Claimed Marks | Artifact Evidence & Location in Submission |
| :--- | :---: | :---: | :--- |
| **1. Problem Formulation & Domain Relevance**<br>Clarity of objective, industry alignment (Tata Technologies Case Study 1), automotive AUTOSAR standard context. | 15 | **15** | `Synopsis/Project_Synopsis.md`<br>`Documentation/Technical_Report_PCCOE_AIML.md` (Chapters 1 & 2) |
| **2. Data Engineering & Knowledge Base**<br>Corpus depth, multi-format ingestion (PDFs + ARXML), metadata preservation across BCM, BMS, ADAS. | 15 | **15** | `Input_Data/` (4 Technical HLD PDFs, 2 ARXML Catalogs, Knowledge Base Metadata JSON)<br>`Code/parsers/` |
| **3. Model, RAG Pipeline & Rule Engine**<br>Hybrid retrieval (Dense Cosine + Lexical BM25), VFB port-interface matching, revision comparison between v2.3 and v2.4. | 25 | **25** | `Code/vector_store.py`<br>`Code/retriever.py`<br>`Code/rag_pipeline.py`<br>`Code/autosar_analyzer.py`<br>`Model_Prompts_Config/` |
| **4. Groundedness & Source Citation Verification**<br>Mandatory document title, section, page citations; absence of hallucinations; citation validator. | 15 | **15** | `Evaluation_Results/sample_grounded_responses_with_citations.md`<br>`Code/evaluation_metrics.py` (Citation Accuracy: 100%) |
| **5. Empirical Evaluation & RAGAS Benchmarking**<br>15-question ground truth dataset, Faithfulness (>85%), Relevancy (>88%), Context Precision (100%), sub-millisecond latency. | 15 | **15** | `Evaluation_Results/test_ground_truth_qa_pairs.json`<br>`Evaluation_Results/evaluation_report.json`<br>`Evaluation_Results/evaluation_metrics_summary.md` |
| **6. User Interface, Working Behaviour & Deployment**<br>Interactive Web GUI (Port 8081), CLI console, 1-click Windows batch launchers, zero external cloud dependencies. | 10 | **10** | `Code/app_web_gui.py`<br>`Code/cli_interactive.py`<br>`Code/run_web_gui.bat` |
| **7. Documentation, Video Script & Compliance**<br>Comprehensive technical report, signed approval forms, student declarations, 8-minute demonstration script. | 5 | **5** | `Documentation/Technical_Report_PCCOE_AIML.md`<br>`Declarations/`<br>`Video/Demonstration_Script_and_Storyboard.md` |
| **TOTAL** | **100** | **100** | **Comprehensive Full-Marks Submission Package** |
