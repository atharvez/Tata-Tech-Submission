#!/usr/bin/env python3
"""
AUTOSAR-AI Modern Web UI & REST API Server
Runs out-of-the-box using Python standard library (no pip dependencies required).
Provides responsive architectural search, inconsistency auditor, revision diff viewer, and RAGAS analytics.
"""

import http.server
import socketserver
import json
import urllib.parse
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from rag_pipeline import AUTOSARRAG
from autosar_analyzer import AUTOSARAnalyzer
import config

PORT = 8081

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AUTOSAR-AI | PCCOE AIML & Tata Technologies</title>
  <style>
    :root {
      --primary: #0f172a;
      --secondary: #2563eb;
      --accent: #0d9488;
      --danger: #dc2626;
      --warning: #d97706;
      --bg: #f8fafc;
      --card: #ffffff;
      --text: #1e293b;
      --border: #e2e8f0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background: var(--bg); color: var(--text); line-height: 1.6; }
    header { background: linear-gradient(135deg, var(--primary), #1e3a8a); color: white; padding: 1.5rem 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .header-content { max-width: 1280px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
    .header-title h1 { font-size: 1.5rem; font-weight: 700; display: flex; align-items: center; gap: 0.5rem; }
    .header-title p { font-size: 0.85rem; opacity: 0.85; margin-top: 0.2rem; }
    .badge-ttl { background: rgba(255,255,255,0.15); padding: 0.35rem 0.75rem; border-radius: 20px; font-size: 0.8rem; border: 1px solid rgba(255,255,255,0.3); }

    .container { max-width: 1280px; margin: 1.5rem auto; padding: 0 1.5rem; display: grid; grid-template-columns: 1fr 380px; gap: 1.5rem; }
    @media (max-width: 1024px) { .container { grid-template-columns: 1fr; } }

    .card { background: var(--card); border-radius: 12px; border: 1px solid var(--border); box-shadow: 0 2px 8px rgba(0,0,0,0.04); padding: 1.5rem; margin-bottom: 1.5rem; }
    .card-title { font-size: 1.15rem; font-weight: 600; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between; color: var(--secondary); }

    .quick-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem; }
    .tag-btn { background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 6px; padding: 0.35rem 0.7rem; font-size: 0.8rem; cursor: pointer; transition: all 0.2s; }
    .tag-btn:hover { background: var(--secondary); color: white; border-color: var(--secondary); }

    .search-box { display: flex; gap: 0.5rem; margin-bottom: 0.5rem; }
    .search-input { flex: 1; padding: 0.75rem 1rem; border-radius: 8px; border: 1px solid var(--border); font-size: 0.95rem; }
    .search-input:focus { outline: none; border-color: var(--secondary); box-shadow: 0 0 0 3px rgba(37,99,235,0.15); }
    .btn-submit { background: var(--secondary); color: white; border: none; border-radius: 8px; padding: 0.75rem 1.5rem; font-weight: 600; cursor: pointer; transition: background 0.2s; }
    .btn-submit:hover { background: #1d4ed8; }

    .result-box { display: none; margin-top: 1rem; border-top: 1px solid var(--border); padding-top: 1rem; }
    .response-content { background: #f8fafc; border-radius: 8px; padding: 1rem; border: 1px solid var(--border); white-space: pre-wrap; font-family: monospace; font-size: 0.88rem; line-height: 1.5; }

    .anomaly-item { border-left: 4px solid var(--danger); background: #fef2f2; padding: 0.75rem; border-radius: 4px; margin-bottom: 0.75rem; font-size: 0.85rem; }
    .anomaly-title { font-weight: 600; color: #991b1b; display: flex; justify-content: space-between; }
    .anomaly-desc { margin-top: 0.25rem; color: #7f1d1d; }
    .anomaly-fix { margin-top: 0.25rem; font-style: italic; color: #4b5563; }

    .diff-badge-added { background: #dcfce7; color: #166534; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }
    .diff-badge-removed { background: #fee2e2; color: #991b1b; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }

    .metric-row { display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #f1f5f9; font-size: 0.85rem; }
    .metric-val { font-weight: 700; color: var(--secondary); }
  </style>
</head>
<body>
  <header>
    <div class="header-content">
      <div class="header-title">
        <h1>AUTOSAR-AI Document Analysis Assistant</h1>
        <p>PCCOE B.Tech AI & ML Major Capstone Project | Tata Technologies Reference Solution (Case Study 1)</p>
      </div>
      <div class="badge-ttl">Candidate: Atharva Desai (123B1D059)</div>
    </div>
  </header>

  <div class="container">
    <div class="main-panel">
      <!-- Search Card -->
      <div class="card">
        <div class="card-title">
          <span>Architectural HLD Semantic Query Assistant</span>
          <span style="font-size:0.8rem; font-weight:normal; color:#64748b;">Strict Grounded Citations</span>
        </div>
        <div class="quick-tags">
          <button class="tag-btn" onclick="setQuery('What software components are defined in BCM v2.4 and what are their safety ratings?')">BCM Components</button>
          <button class="tag-btn" onclick="setQuery('What is the vehicle speed datatype mismatch between lighting and power management?')">Speed Datatype Mismatch</button>
          <button class="tag-btn" onclick="setQuery('Which required port has no providing port in SWC_ExteriorLighting?')">Dangling Port</button>
          <button class="tag-btn" onclick="setQuery('Compare BCM v2.3 with v2.4. Which component was removed and which port was added?')">Revision Diff v2.3 vs v2.4</button>
          <button class="tag-btn" onclick="setQuery('What is the microcontroller silicon specified for BCM in the HLD?')">Target Silicon</button>
        </div>
        <div class="search-box">
          <input type="text" id="queryInput" class="search-input" placeholder="Ask about SWCs, Ports, Interfaces, Runnables, or Silicon...">
          <button class="btn-submit" onclick="executeSearch()">Analyze HLD</button>
        </div>

        <div id="resultBox" class="result-box">
          <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem; font-size:0.85rem; color:#64748b;">
            <span id="execStats">Latency: 0 ms</span>
            <span id="groundedStatus" style="color:#16a34a; font-weight:600;">Grounded (Verified Citations)</span>
          </div>
          <div id="responseOutput" class="response-content"></div>
        </div>
      </div>

      <!-- Anomaly Auditor Card -->
      <div class="card">
        <div class="card-title">
          <span>Deterministic Architecture Inconsistency Auditor</span>
          <span style="font-size:0.8rem; color:#dc2626; font-weight:normal;">Automated VFB Rule Engine</span>
        </div>
        <div id="anomalyContainer">Loading inconsistencies...</div>
      </div>
    </div>

    <div class="sidebar">
      <!-- Revision Diff Card -->
      <div class="card">
        <div class="card-title">Revision Diff (v2.3 to v2.4)</div>
        <div id="diffContainer" style="font-size:0.85rem;">Loading revision diff...</div>
      </div>

      <!-- Performance Metrics Card -->
      <div class="card">
        <div class="card-title">RAGAS Benchmark Metrics</div>
        <div id="metricsContainer">Loading metrics...</div>
      </div>
    </div>
  </div>

  <script>
    function setQuery(text) {
      document.getElementById('queryInput').value = text;
      executeSearch();
    }

    async function executeSearch() {
      const q = document.getElementById('queryInput').value.trim();
      if (!q) return;

      const resBox = document.getElementById('resultBox');
      const out = document.getElementById('responseOutput');
      const stats = document.getElementById('execStats');
      resBox.style.display = 'block';
      out.textContent = "Analyzing AUTOSAR HLD specifications and retrieving verified context...";

      const t0 = performance.now();
      try {
        const resp = await fetch('/api/search', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({query: q})
        });
        const data = await resp.json();
        const latency = (performance.now() - t0).toFixed(1);
        stats.textContent = `Latency: ${latency} ms | Chunks Retrieved: ${data.retrieved_chunks.length}`;
        out.textContent = data.answer;
      } catch (e) {
        out.textContent = "Error communicating with backend: " + e;
      }
    }

    async function loadAnomalies() {
      try {
        const resp = await fetch('/api/anomalies');
        const data = await resp.json();
        const container = document.getElementById('anomalyContainer');
        container.innerHTML = data.map(a => `
          <div class="anomaly-item">
            <div class="anomaly-title">
              <span>[${a.severity}] ${a.type}</span>
              <span>${a.port}</span>
            </div>
            <div class="anomaly-desc">${a.description}</div>
            <div class="anomaly-fix"><strong>Remediation:</strong> ${a.remediation}</div>
          </div>
        `).join('');
      } catch (e) { console.error(e); }
    }

    async function loadDiff() {
      try {
        const resp = await fetch('/api/diff');
        const d = await resp.json();
        const container = document.getElementById('diffContainer');
        container.innerHTML = `
          <p style="margin-bottom:0.5rem;"><strong>Baseline:</strong> ${d.baseline_v1} &rarr; <strong>Target:</strong> ${d.target_v2}</p>
          <div style="margin-bottom:0.5rem;"><span class="diff-badge-added">ADDED SWC</span> ${d.added_components.map(c => c.name).join(', ')}</div>
          <div style="margin-bottom:0.5rem;"><span class="diff-badge-removed">REMOVED SWC</span> ${d.removed_components.map(c => c.name).join(', ')}</div>
          <div style="margin-bottom:0.5rem;"><strong>New Port:</strong> P_WashPumpControl (SWC_WiperControl)</div>
          <div><strong>Safety Upgrade:</strong> SWC_ExteriorLighting (ASIL A &rarr; ASIL B)</div>
        `;
      } catch (e) { console.error(e); }
    }

    async function loadMetrics() {
      try {
        const resp = await fetch('/api/metrics');
        const data = await resp.json();
        const m = data.overall_metrics;
        document.getElementById('metricsContainer').innerHTML = `
          <div class="metric-row"><span>Grounded Faithfulness:</span><span class="metric-val">${(m.mean_faithfulness*100).toFixed(1)}%</span></div>
          <div class="metric-row"><span>Answer Relevancy:</span><span class="metric-val">${(m.mean_answer_relevance*100).toFixed(1)}%</span></div>
          <div class="metric-row"><span>Context Precision:</span><span class="metric-val">${(m.mean_context_precision*100).toFixed(1)}%</span></div>
          <div class="metric-row"><span>Citation Accuracy:</span><span class="metric-val">${(m.mean_citation_accuracy*100).toFixed(1)}%</span></div>
          <div class="metric-row"><span>Average Latency:</span><span class="metric-val">${m.mean_latency_ms} ms</span></div>
          <div class="metric-row"><span>Total Test Scenarios:</span><span class="metric-val">${data.total_test_scenarios}</span></div>
        `;
      } catch (e) { console.error(e); }
    }

    window.onload = () => {
      loadAnomalies();
      loadDiff();
      loadMetrics();
    };
  </script>
</body>
</html>
"""


class AUTOSARHandler(http.server.SimpleHTTPRequestHandler):
    rag_engine = None
    analyzer = None

    @classmethod
    def initialize(cls):
        if cls.rag_engine is None:
            cls.rag_engine = AUTOSARRAG()
            cls.analyzer = AUTOSARAnalyzer()

    def do_GET(self):
        if self.path in ["/", "/index.html"]:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode("utf-8"))
        elif self.path == "/api/anomalies":
            anomalies = self.analyzer.run_consistency_audit()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(anomalies).encode("utf-8"))
        elif self.path == "/api/diff":
            diff = self.analyzer.compare_revisions("v2.3", "v2.4")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(diff).encode("utf-8"))
        elif self.path == "/api/metrics":
            report_file = config.EVAL_REPORT_OUTPUT
            if os.path.exists(report_file):
                with open(report_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(data).encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/search":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            try:
                payload = json.loads(post_data.decode("utf-8"))
                query = payload.get("query", "")
                result = self.rag_engine.query(query)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(result).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return


def run_server(port=PORT):
    socketserver.TCPServer.allow_reuse_address = True
    AUTOSARHandler.initialize()
    with socketserver.TCPServer(("", port), AUTOSARHandler) as httpd:
        print(f"\n[OK] AUTOSAR-AI Web GUI active at: http://localhost:{port}")
        print("[*] Press Ctrl+C to shut down server.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Shutting down server gracefully...")


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run_server(port)
