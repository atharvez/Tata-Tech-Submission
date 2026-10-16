"""
AUTOSAR HLD PDF Parser
Extracts text, section headers, tables, and page metadata from automotive technical PDFs.
"""

import os
from pathlib import Path
from typing import List, Dict, Any

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None


class HLDParser:
    @staticmethod
    def parse_pdf(pdf_path: Path) -> List[Dict[str, Any]]:
        """
        Extracts pages and chunks from an AUTOSAR HLD PDF.
        Returns a list of structured dictionaries with text, page number, and section cues.
        """
        results = []
        if not os.path.exists(pdf_path):
            return results

        filename = os.path.basename(pdf_path)
        title = filename.replace(".pdf", "").replace("_", " ")

        if PdfReader is not None:
            try:
                reader = PdfReader(str(pdf_path))
                for page_idx, page in enumerate(reader.pages):
                    raw_text = page.extract_text() or ""
                    clean_text = raw_text.strip()
                    if not clean_text:
                        continue

                    # Determine section name from content lines
                    lines = [l.strip() for l in clean_text.split("\n") if l.strip()]
                    section_title = f"Page {page_idx + 1}"
                    for line in lines[:5]:
                        if any(line.startswith(prefix) for prefix in ["1.", "2.", "3.", "4.", "5.", "6.", "Section"]):
                            section_title = line
                            break

                    results.append({
                        "document_id": filename.replace(".pdf", ""),
                        "document_title": title,
                        "page_number": page_idx + 1,
                        "section": section_title,
                        "content": clean_text
                    })
            except Exception as e:
                print(f"[!] Warning: pypdf parsing error on {filename}: {e}")

        return results
