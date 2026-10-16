#!/usr/bin/env python3
"""
AUTOSAR-AI Interactive CLI Terminal
Provides interactive architectural consultation with grounded source citations and consistency audits.
"""

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from rag_pipeline import AUTOSARRAG
from autosar_analyzer import AUTOSARAnalyzer


def print_banner():
    banner = """
================================================================================
   🚗  AUTOSAR-AI: ARCHITECTURAL HLD ANALYSIS & VERIFICATION CONSOLE  🚗
        Developed for PCCOE CS-AIML Major Project & Tata Technologies
================================================================================
* Multi-Format Ingestion: AUTOSAR Classic (BCM, BMS) & Adaptive (ADAS L2) PDFs + ARXMLs
* Strict Grounded Answers with Verifiable Section, Page & Diagram Citations
* Automated VFB Port-Interface Consistency Audit & Baseline Revision Diff Engine
================================================================================
    """
    print(banner)


def main():
    print_banner()
    print("[*] Initializing AUTOSAR-AI RAG Pipeline & Consistency Engine...")
    rag = AUTOSARRAG()
    analyzer = AUTOSARAnalyzer()
    print(f"[OK] System Ready! Indexed {rag.total_chunks} architectural passages.\n")

    print("Quick Test Queries:")
    print("  1. 'What software components are defined in BCM v2.4 and their safety ratings?'")
    print("  2. 'What is the vehicle speed datatype mismatch between lighting and power management?'")
    print("  3. 'Which required port in SWC_ExteriorLighting has no providing port?'")
    print("  4. 'Compare BCM v2.3 with v2.4. Which component was removed and which port was added?'")
    print("  5. 'What target microcontroller silicon is specified for the BCM ECU in the HLD?'\n")
    print("Type 'audit' to run VFB consistency check, 'diff' for revision comparison, or 'exit' to quit.\n" + "-" * 80)

    while True:
        try:
            user_input = input("\n🚗 [Enter AUTOSAR Architectural Query] > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "q"]:
                print("\n[!] Exiting AUTOSAR-AI Assistant.")
                break

            if user_input.lower() == "audit":
                print("\n🔍 [Running VFB Port-Interface Consistency Audit]...")
                anomalies = analyzer.run_consistency_audit()
                print(f"[+] Found {len(anomalies)} Architectural Anomalies:\n")
                for a in anomalies:
                    print(f"  • [{a['severity']}] {a['type']}: {a['port']}")
                    print(f"    Description: {a['description']}")
                    print(f"    Remediation: {a['remediation']}\n")
                continue

            if user_input.lower() == "diff":
                print("\n🔍 [Comparing HLD Baselines v2.3 vs v2.4]...")
                diff = analyzer.compare_revisions("v2.3", "v2.4")
                print(f"  • Added Components: {[c['name'] for c in diff['added_components']]}")
                print(f"  • Removed Components: {[c['name'] for c in diff['removed_components']]}")
                print(f"  • Modified Interfaces: {[i['interface'] for i in diff['modified_interfaces']]}\n")
                continue

            print("\n🔍 [AUTOSAR-AI] Analyzing query & retrieving verified context...")
            t0 = time.time()
            result = rag.query(user_input)
            latency_ms = (time.time() - t0) * 1000

            print("\n" + "=" * 80)
            print(result["answer"])
            print("=" * 80)

            print(f"\n⏱️  Latency: {latency_ms:.2f} ms")
            print(f"🛡️  Groundedness Score: {result['groundedness_score']*100:.1f}%")
            print(f"📚  Verified Citations: {len(result['citations'])} source reference(s)\n")
            print("-" * 80)

        except (KeyboardInterrupt, EOFError):
            print("\n\n[!] Session terminated by user.")
            break


if __name__ == "__main__":
    main()
