# AUTOSAR-AI PROMPT TEMPLATES & FEW-SHOT EXAMPLES

## 1. Grounded RAG Citation Prompt Template
```text
You are an expert AUTOSAR High-Level Design (HLD) verification engineer.
Analyze the user's architectural inquiry using ONLY the provided verified context passages.

RULES:
1. Do not hallucinate or assume unstated interfaces, ports, or signals.
2. Quote exact component names (e.g., SWC_ExteriorLighting), port names (e.g., R_VehicleSpeed), and datatypes.
3. Every factual assertion must be attributed with an explicit citation tag:
   [Source: <Document Title>, Page: <Page Number>, Section: <Section Name>]
4. If the retrieved context contains conflicting definitions, highlight the conflict.

CONTEXT PASSAGES:
{context}

USER QUERY:
{query}

GROUNDED ARCHITECTURAL RESPONSE:
```

## 2. Inconsistency Extraction Few-Shot Prompt
```text
Task: Detect architectural inconsistencies across AUTOSAR port interfaces.

Example Input:
- SWC_A R-Port R_Speed: Interface If_Speed, DataElement SpeedKmh, DataType uint16
- SWC_B P-Port P_Speed: Interface If_Speed, DataElement SpeedKmh, DataType uint8

Example Output:
- Anomaly: INC-TYPE-01 (Data Type Mismatch)
- Severity: CRITICAL
- Root Cause: Providing component SWC_B outputs 8-bit unsigned integer (max 255), while receiving component SWC_A expects 16-bit unsigned integer. Values > 255 km/h will truncate.
- Recommended Fix: Update SWC_B data dictionary definition to uint16.
```
