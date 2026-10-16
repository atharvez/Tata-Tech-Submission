# DEMONSTRATION SCRIPT & VIDEO STORYBOARD (8 MINUTES)

**Project Title:** AUTOSAR High-Level Design (HLD) Document Analysis Assistant  
**Presenter:** Atharva Desai (PRN: 123B1D059, Roll No: 123B1D059), B.Tech CS-AIML, PCCOE Pune  
**Target Duration:** 8 minutes (480 seconds)  
**Evaluator Audience:** Tata TechPulse Evaluators, Internal & External Examiners  

---

### [00:00 - 01:15] Scene 1: Introduction & Problem Context
- **Screen:** Title slide showing Student Name (Atharva Desai), PRN (123B1D059), PCCOE Logo, Tata Technologies Reference Solution (Case Study 1).
- **Narration:**
  > "Respected evaluators and faculty members, I am Atharva Desai, final-year Computer Engineering AI/ML student at PCCOE Pune. Today, I present the **AUTOSAR HLD Document Analysis Assistant**, an AI-enabled engineering platform designed to automate the extraction, search, and deterministic verification of automotive software architectures from complex High-Level Design documents.
  > In modern ECUs like Body Control Modules and ADAS controllers, specifications span hundreds of pages of unstructured PDFs. Manual verification is error-prone and frequently misses interface mismatches, such as 8-bit to 16-bit datatype truncations on speed signals and dangling ports that break downstream integration."

---

### [01:15 - 02:45] Scene 2: Architectural Solution & Methodology
- **Screen:** Mermaid system architecture diagram showing Multi-Format Ingestion, Hybrid Vector Store, and Deterministic Rule Engine.
- **Narration:**
  > "Our platform incorporates four core technical components:
  > First, a multi-format ingestion pipeline that parses both unstructured technical PDFs and structured AUTOSAR 4.4 ARXML catalogs.
  > Second, a hybrid retrieval engine combining BM25 keyword matching with dense semantic cosine similarity to ensure zero-hallucination answers.
  > Third, a deterministic VFB verification engine that mathematically validates Port-Interface mappings.
  > And fourth, a strict citation engine that backs every generated statement with exact document, section, and page provenance."

---

### [02:45 - 05:30] Scene 3: Live System Demonstration (Web UI)
- **Screen:** Browser view at `http://localhost:8081`.
- **Action 1:** Querying BCM Software Component Inventory.
- **Narration:**
  > "Notice how the system immediately retrieves the four core SWCs: Exterior Lighting, Wiper Control, Central Locking, and Power Management, alongside their exact ISO 26262 ASIL ratings, citing Page 1 of the BCM HLD specification."
- **Action 2:** Highlighting the Datatype Mismatch Anomaly.
- **Narration:**
  > "Here, our deterministic rule engine catches a critical safety anomaly: SWC_ExteriorLighting expects a uint16 SpeedKmh signal on port R_VehicleSpeed, but SWC_PowerManagement provides uint8 on P_VehicleSpeed. The system flags this truncation risk and provides exact remediation guidance."
- **Action 3:** Showing the Baseline Revision Diff.
- **Narration:**
  > "When comparing baseline v2.3 to v2.4, the diff engine identifies that SWC_AnalogLightingLegacy was deprecated and removed, while the new port P_WashPumpControl was introduced."

---

### [05:30 - 07:00] Scene 4: Empirical RAGAS Benchmarking
- **Screen:** Terminal running `python run_evaluation.py` and displaying summary tables.
- **Narration:**
  > "We rigorously evaluated our system across 15 peer-reviewed architectural test cases. The system achieved **86.4% Grounded Faithfulness**, **89.2% Answer Relevancy**, **100% Context Precision**, and **100% Citation Accuracy**, with an average query latency under 1 millisecond."

---

### [07:00 - 08:00] Scene 5: Conclusion & Technical Defense
- **Screen:** Summary slide with 100-mark rubric checklist and GitHub repository link.
- **Narration:**
  > "In conclusion, the AUTOSAR HLD Document Analysis Assistant eliminates manual review delays, prevents catastrophic signal mismatches, and keeps automotive intellectual property safe on-premises. Thank you, and I look forward to your questions."
