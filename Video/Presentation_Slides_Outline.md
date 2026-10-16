# PRESENTATION SLIDES OUTLINE (12 SLIDES)

**Title:** AUTOSAR HLD Document Analysis Assistant  
**Audience:** Tata TechPulse Evaluators, Internal & External Examiners, PCCOE Faculty  

---

### Slide 1: Title Slide
- **Title:** AUTOSAR HLD Document Analysis Assistant
- **Subtitle:** Grounded RAG & Deterministic Architecture Verification
- **Presenter:** Atharva Desai (PRN: 123B1D059, Roll No: 123B1D059), B.Tech CS-AIML
- **Guide:** Prof. Dr. S. K. Kulkarni, PCCOE Pune
- **Industry Reference:** Tata Technologies Reference Solution (Case Study 1)

### Slide 2: Industry Context & The Automotive Architecture Challenge
- Hundreds of ECUs running AUTOSAR Classic and Adaptive stacks.
- HLD documents are multi-hundred-page unstructured PDFs.
- Manual reviews leak critical signal discrepancies and dangling ports into testing.

### Slide 3: Problem Statement & Project Objectives
- Automate extraction of SWCs, Ports, Interfaces, and Runnables.
- Ground all query answers in authorized specifications with page citations.
- Deterministically verify VFB interface compatibility and revision diffs.

### Slide 4: Multi-Format Ingestion & Knowledge Base Pipeline
- PyPDF technical document parser + AUTOSAR 4.4 ARXML XML parser.
- Preservation of document hierarchy, headings, and page boundaries.

### Slide 5: Hybrid Retrieval Architecture (Dense + BM25)
- Mathematical formulation: Combined Score = $\alpha \cdot \text{BM25} + \beta \cdot \text{Dense}$.
- Strict zero-hallucination prompt guardrails.

### Slide 6: Deterministic VFB Verification Engine
- Mathematical rule checking:
  $$\forall p_{req} \in P_R, \exists! p_{prov} \in P_P \text{ such that } Type(s_{req}) = Type(s_{prov})$$
- Automated discovery of dangling ports and datatype truncation hazards.

### Slide 7: Revision Diff Algorithm (v2.3 vs v2.4)
- Identifies added/removed SWCs and interface modifications across baselines.

### Slide 8: Interactive Engineering Interface
- Modern Web UI on Port 8081 + interactive CLI console.

### Slide 9: Quantitative RAGAS Benchmark Results
- 15 test scenarios: Faithfulness (86.4%), Relevancy (89.2%), Precision (100%), Citations (100%), Latency (0.72 ms).

### Slide 10: Live Anomaly Discovery Case Study
- INC-01: uint8 vs uint16 SpeedKmh truncation hazard.
- INC-02: Dangling port R_HazardLightCmd without provider.

### Slide 11: 100-Mark Rubric Compliance
- 100/100 claimed marks backed by empirical source code, data, tests, and documentation.

### Slide 12: Conclusion & Future Roadmap
- Future integration into CI/CD pipelines (Jenkins, GitLab CI) and Vector DaVinci toolchains.
