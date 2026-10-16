"""
AUTOSAR ARXML Parser
Extracts Software Components, Port Prototypes, and Interface Definitions from ARXML specifications.
"""

import os
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Any


class ARXMLParser:
    @staticmethod
    def parse_arxml(arxml_path: Path) -> List[Dict[str, Any]]:
        """
        Parses an AUTOSAR XML file and extracts component models into clean text chunks for vector indexing.
        """
        chunks = []
        if not os.path.exists(arxml_path):
            return chunks

        filename = os.path.basename(arxml_path)
        doc_id = filename.replace(".arxml", "")

        try:
            tree = ET.parse(str(arxml_path))
            root = tree.getroot()

            # Iterate through SWC elements regardless of namespace
            for elem in root.iter():
                tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
                if "COMPONENT-TYPE" in tag:
                    swc_name_elem = elem.find(".//{*}SHORT-NAME") or elem.find("SHORT-NAME")
                    swc_name = swc_name_elem.text if swc_name_elem is not None else "UnknownSWC"

                    ports_info = []
                    for port_elem in elem.iter():
                        p_tag = port_elem.tag.split("}")[-1] if "}" in port_elem.tag else port_elem.tag
                        if "PORT-PROTOTYPE" in p_tag:
                            p_name = port_elem.find(".//{*}SHORT-NAME") or port_elem.find("SHORT-NAME")
                            p_name_text = p_name.text if p_name is not None else "Port"
                            p_dir = "P-Port" if "P-PORT" in p_tag else "R-Port"
                            ports_info.append(f"- {p_dir}: {p_name_text}")

                    content_lines = [
                        f"AUTOSAR Software Component: {swc_name}",
                        f"Category: {tag}",
                        f"Defined Ports ({len(ports_info)}):"
                    ] + ports_info

                    chunk_text = "\n".join(content_lines)
                    chunks.append({
                        "document_id": doc_id,
                        "document_title": f"AUTOSAR ARXML Catalog ({filename})",
                        "page_number": 1,
                        "section": f"Component: {swc_name}",
                        "content": chunk_text
                    })

        except Exception as e:
            print(f"[!] Warning: Error parsing ARXML file {filename}: {e}")

        return chunks
