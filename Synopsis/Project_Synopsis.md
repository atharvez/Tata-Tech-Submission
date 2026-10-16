# Pimpri Chinchwad College of Engineering (PCCOE), Pune
### Department of Artificial Intelligence & Machine Learning
---
## MAJOR CAPSTONE PROJECT SYNOPSIS
**Academic Year:** 2026 – 2027  
**Program:** B.Tech in Artificial Intelligence & Machine Learning  
**Project Title:** AUTOSAR High-Level Design (HLD) Document Analysis Assistant Using Retrieval-Augmented Generation (RAG) and Deterministic Architecture Verification  
**Industry Reference:** Automotive Engineering AI Reference Solutions (TTL-Classification: Public – Case Study 1)  
**Student Name:** [Student Name]  
**PRN:** 123B1F001  
**Guide / Mentor:** Prof. Dr. S. K. Kulkarni / Industry Mentor (Tata Technologies Ltd.)  

---

### 1. Executive Summary & Abstract
Modern Automotive Electronic Control Units (ECUs) are built upon the open AUTOSAR (AUTomotive Open System ARchitecture) standard. Developing software for safety-critical domains such as Body Control Modules (BCM), Powertrain Gateways, and ADAS requires maintaining and reviewing High-Level Design (HLD) documents that frequently span hundreds of pages of unstructured text, tables, port-interface specifications, and signal matrices. 

System architects, developers, integrators, and safety reviewers currently invest hundreds of hours manually verifying these specifications. Manual review is highly prone to human fatigue, resulting in inconsistent terminology, unmapped Required/Provided Ports (R-Ports and P-Ports), mismatched Sender-Receiver data types, missing signal routings, and fragmented traceability to downstream verification test cases.

This project implements an end-to-end, enterprise-grade **AUTOSAR HLD Document Analysis Assistant** compliant with the reference technology position of Tata Technologies Ltd. (TTL). The solution integrates:
1. **Context-Aware Document Ingestion & Parsing:** Advanced parsing of complex automotive technical PDFs and ARXML component catalogs with page-level metadata extraction.
2. **Local Vector Knowledge Store:** High-performance semantic indexing using `SentenceTransformers (BGE/all-MiniLM)` and `FAISS` local vector database, ensuring zero data exfiltration of proprietary automotive IP.
3. **Cited Retrieval-Augmented Generation (RAG):** Multi-stage retrieval combining dense vector similarity with keyword BM25 filtering, generating answers strictly grounded in approved HLDs with verifiable section and page citations.
4. **Deterministic Architectural Verification Engine:** A rule-based graph validation system (built on `NetworkX`) that automatically maps SWC dependencies, flags dangling ports, identifies unmapped interfaces, and detects interface mismatches between legacy and revised HLD versions.
5. **Human-in-the-Loop Review & Export Workflow:** A full-stack web interface built with **FastAPI** backend and **Streamlit** engineering portal, coupled with an **SQLite** audit database supporting engineering disposition (Accept / Reject / Modify) and structured export to JSON, CSV, and audit-ready PDF reports.

---

### 2. Problem Statement
Automotive software engineering teams face three primary challenges when handling AUTOSAR HLD documents:
1. **Information Fragmentation and Low Searchability:** Architectural knowledge is buried in unstructured PDF documents and legacy repositories. Locating interface descriptions, sender-receiver signals, and execution timing requirements takes significant manual effort.
2. **Subtle Interface Inconsistencies:** Complex multi-ECU interactions lead to subtle errors—such as an R-Port requesting a `uint16` vehicle speed signal while the corresponding P-Port emits an `int8` datatype, or orphaned runnables without OS task allocation. These defects often leak into integration testing or Hardware-in-the-Loop (HIL) stages, causing costly project delays.
3. **Data Privacy and IP Constraints in Cloud AI:** Traditional cloud-based LLM APIs (e.g., standard public endpoints) present compliance risks regarding automotive intellectual property and strict confidentiality requirements. A localized, containerized on-premises solution is mandatory.

---

### 3. Project Objectives
- **Objective 1:** Develop a robust parsing pipeline for automotive HLD PDFs and ARXML specifications that preserves hierarchical sections, tables, component definitions, and port interfaces.
- **Objective 2:** Build a localized semantic search and question-answering assistant using FAISS and local embeddings with strict citation grounding (page and section level attribution).
- **Objective 3:** Implement an automated Architectural Entity Extraction module to identify Software Components (Application SWC, Sensor-Actuator SWC, Complex Device Drivers), Ports, Interfaces, and Signals.
- **Objective 4:** Develop a deterministic consistency verification and revision comparison engine to detect unmapped ports, interface mismatches, and revision regressions between document versions.
- **Objective 5:** Provide a user-friendly Streamlit web interface with interactive dependency graphs, human-in-the-loop review queues, and export capabilities for audit readiness.
- **Objective 6:** Evaluate system performance across retrieval accuracy (Recall@K, MRR), answer groundedness, entity extraction F1-score, and defect discovery precision against expert ground truth.

---

### 4. Scope of the Project
#### In Scope:
- Ingestion of multi-page technical specification PDFs and structured ARXML files.
- Document chunking strategy preserving AUTOSAR architectural context.
- Local dense vector retrieval with FAISS and SentenceTransformers.
- Natural language query interface with cited source excerpts and confidence scoring.
- Automated extraction and tabular inventory of SWCs, Ports, Interfaces, and Signals.
- Deterministic graph-based consistency verification (dangling ports, signal type mismatches, circular dependencies).
- Version-to-version revision comparison between successive HLD releases (e.g., v2.3 vs v2.4).
- Human review disposition workflow (Accept/Flag/Reject) stored in SQLite audit database.
- Export of findings into JSON, CSV, and formal PDF summary reports.
- Containerization using Docker for air-gapped on-premises deployment.

#### Out of Scope:
- Autonomous modification of original source HLD files without engineering oversight.
- Direct flashing or automatic code generation onto physical ECU silicon.
- Replacement of formal AUTOSAR authoring tools (e.g., Vector DaVinci, EB tresos) or certified ISO 26262 assessors.

---

### 5. Methodology & System Architecture

```
+-----------------------------------------------------------------------------------+
|                            ENGINEERING USER (WEB BROWSER)                         |
+-----------------------------------------------------------------------------------+
                                         | HTTP / REST
                                         v
+-----------------------------------------------------------------------------------+
|                   STREAMLIT ENGINEERING UI (MODULAR PAGES)                       |
|  [Ingestion] | [SWC Inventory] | [Cited RAG Chat] | [Consistency & Diff] | [Review] |
+-----------------------------------------------------------------------------------+
                                         | REST API
                                         v
+-----------------------------------------------------------------------------------+
|                        FASTAPI BACKEND APPLICATION SERVICES                       |
|   Routers: /ingestion | /architecture | /qa | /validation | /review | /export     |
+-----------------------------------------------------------------------------------+
       |                                   |                                |
       v                                   v                                v
+----------------------+         +-----------------------+        +-----------------+
| INGESTION & PARSER   |         | RAG & VECTOR ENGINE   |        | DETERMINISTIC   |
| - PyPDF / PDFPlumber |         | - SentenceTransformers|        | VERIFICATION    |
| - ARXML XML Parser   |         | - FAISS Local Index   |        | - NetworkX Graph|
| - Context Chunker    |         | - Hybrid BM25 Filter  |        | - Port Matcher  |
+----------------------+         | - LLM Prompt Guardrail|        | - Diff Engine   |
                                 +-----------------------+        +-----------------+
                                           |                                |
                                           v                                v
                                 +-----------------------+        +-----------------+
                                 | LOCAL VECTOR DB       |        | SQLITE AUDIT DB |
                                 | - faiss_index.bin     |        | - Projects      |
                                 | - metadata_store.json |        | - Dispositions  |
                                 +-----------------------+        | - Findings Log  |
                                                                  +-----------------+
```

#### Detailed Workflow:
1. **Document Ingestion:** The engineer uploads an approved HLD document (PDF or ARXML). The ingestion engine extracts text, tables, component definitions, and page headers.
2. **Context-Aware Chunking:** Chunks are created along architectural boundaries (Software Component blocks, interface tables, signal routing sections) preserving document hierarchy and metadata.
3. **Local Vector Indexing:** Chunks are transformed into 384-dimensional dense vectors using a local SentenceTransformer model and stored in a FAISS index with metadata tags.
4. **Cited Query Processing:** User queries are matched against the FAISS index. The top-$k$ relevant chunks are retrieved and passed with strict instruction templates to the generation model. Answers are returned with mandatory page/section citations.
5. **Deterministic Graph Analysis:** The system parses Port-Interface connections into a directed multigraph using NetworkX. Formal checks verify:
   $$\forall p_{req} \in P_{R}, \exists! p_{prov} \in P_{P} \quad \text{such that} \quad Interface(p_{req}) = Interface(p_{prov}) \wedge Type(s_{req}) = Type(s_{prov})$$
6. **Human Review & Disposition:** Identified discrepancies and answers are reviewed by an engineer who can mark them as Accepted, Suppressed, or Modified. Every decision is immutably logged into the SQLite audit store.

---

### 6. Hardware & Software Requirements
- **Software Requirements:**
  - Operating System: Windows 10/11 or Ubuntu Linux 22.04 LTS
  - Programming Language: Python 3.10 / 3.11 / 3.12
  - Backend Framework: FastAPI 0.115+, Uvicorn
  - Frontend Framework: Streamlit 1.35+
  - Vector Database & Search: FAISS-CPU 1.8+, Sentence-Transformers 3.0+
  - Document Processing: PyPDF 4.2+, PDFPlumber 0.11+, lxml
  - Graph Analysis: NetworkX 3.2+
  - Database: SQLite 3 with SQLAlchemy 2.0+
  - Containerization: Docker 26+, Docker Compose
- **Hardware Requirements:**
  - Processor: Intel Core i5/i7 (8th Gen or higher) / AMD Ryzen 5/7 (4 cores minimum)
  - Memory (RAM): Minimum 8 GB (16 GB recommended for multi-document indexing)
  - Storage: Minimum 10 GB free SSD storage

---

### 7. Project Plan & Milestones (Gantt Chart Representation)

| Phase | Milestone | Duration | Key Deliverables |
|:---|:---|:---|:---|
| **Phase 1** | Requirement Analysis & Architecture Design | Weeks 1–2 | SRS, SDD, Literature survey, AUTOSAR schema definition |
| **Phase 2** | Ingestion, Parsers & Vector Engine | Weeks 3–5 | PDF/ARXML parsers, chunking pipeline, FAISS integration |
| **Phase 3** | Deterministic Rule Engine & Graph Tracer | Weeks 6–8 | SWC extractor, port-interface matcher, revision diff engine |
| **Phase 4** | FastAPI Backend & Streamlit Web UI | Weeks 9–11 | REST endpoints, responsive multi-page UI, SQLite audit store |
| **Phase 5** | Verification, Benchmarking & Evaluation | Weeks 12–14 | Ground-truth testing, RAG groundedness metrics, ROC curves |
| **Phase 6** | Documentation, Packaging & Final Viva | Weeks 15–16 | Final report, user manual, video walkthrough, Docker package |

---

### 8. Expected Outcomes & Deliverables
1. Complete source code repository with FastAPI backend, Streamlit frontend, and automated test suite.
2. Functional prototype capable of ingesting Body Control Module (BCM), ADAS, and Battery Management System (BMS) HLDs.
3. Accurate extraction of SWCs, Ports, Interfaces, and Signals with >90% precision and recall.
4. Cited RAG assistant achieving zero ungrounded hallucinations with verifiable document citations.
5. Automated inconsistency detector identifying mismatched datatypes and unmapped ports.
6. Formal documentation package: SRS, SDD, API Documentation, User Manual, Benchmarking Report, Video Script, and Declarations.

---
**Approved by Guide:** ______________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Head of Department:** ______________________
