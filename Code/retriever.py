"""
AUTOSAR-AI Hybrid Retriever
Combines BM25 lexical keyword matching with dense semantic cosine similarity
to retrieve top-k context passages with page and section provenance.
"""

import math
from typing import List, Dict, Any, Tuple
import config
from vector_store import HybridVectorStore, DocumentChunk


class HybridRetriever:
    def __init__(self, vector_store: HybridVectorStore):
        self.store = vector_store

    def _bm25_score(self, query_tokens: List[str], chunk: DocumentChunk) -> float:
        score = 0.0
        k1 = 1.5
        b = 0.75
        avg_dl = 45.0
        doc_len = len(chunk.tokens)

        for qt in query_tokens:
            if qt in chunk.tokens:
                freq = chunk.tokens.count(qt)
                idf = self.store.idf.get(qt, 1.0)
                numerator = freq * (k1 + 1)
                denominator = freq + k1 * (1 - b + b * (doc_len / avg_dl))
                score += idf * (numerator / denominator)
        return score

    def retrieve(self, query: str, top_k: int = config.DEFAULT_TOP_K) -> List[Dict[str, Any]]:
        """
        Executes hybrid retrieval:
        Combined_Score = (BM25_ALPHA * Normalized_BM25) + (DENSE_BETA * Dense_Cosine)
        """
        if not self.store.chunks:
            return []

        q_tokens = DocumentChunk._tokenize(query)
        dense_results = self.store.search_dense(query, top_k=len(self.store.chunks))
        dense_scores_map = {chunk.chunk_id: score for chunk, score in dense_results}

        bm25_scores = []
        for chunk in self.store.chunks:
            s = self._bm25_score(q_tokens, chunk)
            bm25_scores.append((chunk, s))

        max_bm25 = max([s for _, s in bm25_scores], default=1.0) or 1.0
        max_dense = max(dense_scores_map.values(), default=1.0) or 1.0

        hybrid_ranked = []
        for chunk, bm25_raw in bm25_scores:
            dense_raw = dense_scores_map.get(chunk.chunk_id, 0.0)
            norm_bm25 = bm25_raw / max_bm25
            norm_dense = dense_raw / max_dense

            combined = (config.BM25_ALPHA * norm_bm25) + (config.DENSE_BETA * norm_dense)
            if combined > 0.02:
                hybrid_ranked.append((chunk, combined))

        hybrid_ranked.sort(key=lambda x: x[1], reverse=True)
        top_chunks = hybrid_ranked[:top_k]

        formatted = []
        for chunk, score in top_chunks:
            meta = chunk.metadata
            citation_tag = (
                f"[Source: {meta.get('document_title', 'HLD Spec')}, "
                f"Page: {meta.get('page_number', 1)}, "
                f"Section: {meta.get('section', 'General')}]"
            )
            formatted.append({
                "chunk_id": chunk.chunk_id,
                "text": chunk.text,
                "metadata": meta,
                "score": round(score, 4),
                "citation": citation_tag
            })

        return formatted
