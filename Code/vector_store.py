"""
AUTOSAR-AI Vector Store Implementation
Provides self-contained dense vector indexing, BM25 term weighting, cosine similarity,
and metadata-preserved chunk storage.
"""

import math
import re
import json
from typing import List, Dict, Any, Tuple


class DocumentChunk:
    def __init__(
        self,
        chunk_id: str,
        text: str,
        metadata: Dict[str, Any]
    ):
        self.chunk_id = chunk_id
        self.text = text
        self.metadata = metadata
        self.tokens = self._tokenize(text)

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        return re.findall(r'[a-zA-Z0-9_\-]+', text.lower())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chunk_id": self.chunk_id,
            "text": self.text,
            "metadata": self.metadata
        }


class HybridVectorStore:
    def __init__(self):
        self.chunks: List[DocumentChunk] = []
        self.vocabulary: Dict[str, int] = {}
        self.idf: Dict[str, float] = {}
        self.doc_vectors: List[Dict[int, float]] = []

    def add_parsed_pages(self, pages: List[Dict[str, Any]]) -> int:
        """
        Ingests parsed pages from HLD PDFs and ARXML catalogs into indexed chunks.
        """
        new_count = 0
        for doc in pages:
            doc_id = doc.get("document_id", "DOC-UNK")
            title = doc.get("document_title", "AUTOSAR Specification")
            section = doc.get("section", "General")
            page = doc.get("page_number", 1)
            content = doc.get("content", "")

            # Split larger text into paragraphs
            paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
            if not paragraphs:
                paragraphs = [content.strip()]

            for idx, para in enumerate(paragraphs):
                chunk_id = f"{doc_id}_P{page}_{idx+1}"
                meta = {
                    "document_id": doc_id,
                    "document_title": title,
                    "section": section,
                    "page_number": page
                }
                chunk = DocumentChunk(chunk_id=chunk_id, text=para, metadata=meta)
                self.chunks.append(chunk)
                new_count += 1

        self._build_index()
        return new_count

    def _build_index(self):
        """Constructs inverted index, TF-IDF weights, and vector representations."""
        if not self.chunks:
            return

        vocab = {}
        doc_freq = {}
        total_docs = len(self.chunks)

        for chunk in self.chunks:
            seen_tokens = set()
            for token in chunk.tokens:
                if token not in vocab:
                    vocab[token] = len(vocab)
                if token not in seen_tokens:
                    doc_freq[token] = doc_freq.get(token, 0) + 1
                    seen_tokens.add(token)

        self.vocabulary = vocab
        self.idf = {
            token: math.log((total_docs + 1) / (freq + 1)) + 1.0
            for token, freq in doc_freq.items()
        }

        # Build TF-IDF document vectors
        self.doc_vectors = []
        for chunk in self.chunks:
            vec = {}
            token_counts = {}
            for t in chunk.tokens:
                token_counts[t] = token_counts.get(t, 0) + 1

            for t, count in token_counts.items():
                if t in self.vocabulary:
                    tid = self.vocabulary[t]
                    tf = 1.0 + math.log(count)
                    vec[tid] = tf * self.idf.get(t, 1.0)

            # Normalize vector
            norm = math.sqrt(sum(v * v for v in vec.values()))
            if norm > 0:
                vec = {k: v / norm for k, v in vec.items()}
            self.doc_vectors.append(vec)

    def search_dense(self, query: str, top_k: int = 5) -> List[Tuple[DocumentChunk, float]]:
        """Calculates cosine similarity between query and indexed document chunks."""
        if not self.chunks or not self.doc_vectors:
            return []

        q_tokens = DocumentChunk._tokenize(query)
        q_counts = {}
        for t in q_tokens:
            q_counts[t] = q_counts.get(t, 0) + 1

        q_vec = {}
        for t, count in q_counts.items():
            if t in self.vocabulary:
                tid = self.vocabulary[t]
                tf = 1.0 + math.log(count)
                q_vec[tid] = tf * self.idf.get(t, 1.0)

        q_norm = math.sqrt(sum(v * v for v in q_vec.values()))
        if q_norm > 0:
            q_vec = {k: v / q_norm for k, v in q_vec.items()}
        else:
            return []

        scores = []
        for idx, d_vec in enumerate(self.doc_vectors):
            dot = sum(q_vec[k] * d_vec.get(k, 0.0) for k in q_vec if k in d_vec)
            if dot > 0.01:
                scores.append((self.chunks[idx], dot))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
