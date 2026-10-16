import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable

def generate_synopsis_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1 # Center
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#2563EB'),
        alignment=1
    )
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#4B5563'),
        alignment=1
    )
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=12,
        spaceAfter=6
    )
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1F2937'),
        spaceAfter=6
    )
    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#1F2937'),
        leftIndent=15,
        spaceAfter=4
    )
    
    story = []
    
    story.append(Paragraph("PIMPRI CHINCHWAD COLLEGE OF ENGINEERING (PCCOE), PUNE", title_style))
    story.append(Paragraph("DEPARTMENT OF ARTIFICIAL INTELLIGENCE & MACHINE LEARNING", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("B.Tech Capstone Project Synopsis | Academic Year: 2026 - 2027", meta_style))
    story.append(Paragraph("Industry Reference: Automotive Engineering AI Reference Solutions (TTL-Classification: Public - Case Study 1)", meta_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E3A8A'), spaceBefore=2, spaceAfter=8))
    
    # Metadata Table
    meta_data = [
        [Paragraph("<b>Project Title:</b>", body_style), Paragraph("AUTOSAR HLD Document Analysis Assistant Using Local RAG and Deterministic Verification", body_style)],
        [Paragraph("<b>Student Name:</b>", body_style), Paragraph("Candidate Student Name (PRN: 123B1F001)", body_style)],
        [Paragraph("<b>Academic Guide:</b>", body_style), Paragraph("Prof. Dr. S. K. Kulkarni, Dept of AI & ML, PCCOE", body_style)],
        [Paragraph("<b>Industry Mentor:</b>", body_style), Paragraph("Lead Automotive System Architect, Tata Technologies Ltd.", body_style)],
        [Paragraph("<b>Domain & Stack:</b>", body_style), Paragraph("Automotive AI, AUTOSAR Classic/Adaptive, FastAPI, Streamlit, FAISS, SentenceTransformers", body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[130, 400])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F3F4F6')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#D1D5DB')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E7EB')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("1. Executive Summary & Abstract", h1_style))
    story.append(Paragraph(
        "Modern Automotive Electronic Control Units (ECUs) are developed based on the AUTOSAR standard. "
        "High-Level Design (HLD) documents define Software Components (SWCs), Ports, Interfaces, and Signal matrices across hundreds of pages of unstructured PDFs. "
        "Manual verification causes delays, terminology inconsistencies, unmapped ports, and integration failures. "
        "This project delivers an enterprise-grade AI assistant that combines context-aware PDF/ARXML ingestion, local FAISS vector search, cited Retrieval-Augmented Generation (RAG), "
        "and a deterministic NetworkX graph verification engine to validate interface completeness and revision changes without exposing proprietary code to public cloud services.",
        body_style
    ))
    
    story.append(Paragraph("2. Objectives", h1_style))
    story.append(Paragraph("&bull; Ingest and structure complex automotive HLD PDFs and ARXML component specifications.", bullet_style))
    story.append(Paragraph("&bull; Index architectural knowledge into a persistent local FAISS vector store with SentenceTransformers.", bullet_style))
    story.append(Paragraph("&bull; Deliver natural language Q&A with strict page/section citations and confidence scoring.", bullet_style))
    story.append(Paragraph("&bull; Automatically extract SWC inventories, Port definitions (P-Port, R-Port), and Sender-Receiver interfaces.", bullet_style))
    story.append(Paragraph("&bull; Perform deterministic consistency checks to identify unmapped ports, type mismatches, and revision regressions.", bullet_style))
    story.append(Paragraph("&bull; Provide an intuitive Streamlit UI, FastAPI service layer, human review workflow, and structured audit export.", bullet_style))
    
    story.append(Paragraph("3. Scope & Technology Position", h1_style))
    scope_data = [
        [Paragraph("<b>In Scope</b>", body_style), Paragraph("<b>Out of Scope</b>", body_style)],
        [
            Paragraph("&bull; Ingestion of HLD PDFs & ARXML catalogs<br/>&bull; Local vector embeddings (BGE / MiniLM)<br/>&bull; Grounded Q&A with citations<br/>&bull; SWC, Port, Interface extraction<br/>&bull; Consistency & revision diff reporting<br/>&bull; Human review disposition & PDF export", body_style),
            Paragraph("&bull; Autonomous unreviewed code modifications<br/>&bull; Physical ECU silicon flashing<br/>&bull; Replacement of formal safety assessor approvals<br/>&bull; Cloud transmission of proprietary IP", body_style)
        ]
    ]
    scope_table = Table(scope_data, colWidths=[265, 265])
    scope_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#DBEAFE')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#93C5FD')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#BFDBFE')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(scope_table)
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("4. Implementation Milestones & Timeline", h1_style))
    plan_data = [
        [Paragraph("<b>Stage</b>", body_style), Paragraph("<b>Key Activities</b>", body_style), Paragraph("<b>Deliverable</b>", body_style)],
        [Paragraph("Stage 1 (Weeks 1-4)", body_style), Paragraph("Taxonomy, HLD dataset creation, PDF/ARXML parsers, chunking", body_style), Paragraph("Ingestion Pipeline", body_style)],
        [Paragraph("Stage 2 (Weeks 5-8)", body_style), Paragraph("Local FAISS vector store, SentenceTransformers, Cited RAG pipeline", body_style), Paragraph("Grounded Q&A Engine", body_style)],
        [Paragraph("Stage 3 (Weeks 9-12)", body_style), Paragraph("NetworkX graph engine, consistency checks, revision diff algorithm", body_style), Paragraph("Verification Engine", body_style)],
        [Paragraph("Stage 4 (Weeks 13-16)", body_style), Paragraph("FastAPI backend, Streamlit UI, evaluation benchmarks, packaging", body_style), Paragraph("Complete System", body_style)],
    ]
    plan_table = Table(plan_data, colWidths=[90, 310, 130])
    plan_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E0E7FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#C7D2FE')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E0E7FF')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(plan_table)
    story.append(Spacer(1, 15))
    
    # Signatures
    sig_data = [
        [Paragraph("____________________________<br/><b>Student Signature</b><br/>PRN: 123B1F001", body_style),
         Paragraph("____________________________<br/><b>Project Guide</b><br/>Prof. Dr. S. K. Kulkarni", body_style),
         Paragraph("____________________________<br/><b>Head of Department</b><br/>Dept. of AI & ML, PCCOE", body_style)]
    ]
    sig_table = Table(sig_data, colWidths=[175, 175, 180])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(sig_table)
    
    doc.build(story)
    print("Generated Synopsis PDF at:", output_path)

if __name__ == '__main__':
    out_dir = r"C:\Users\7atha\.gemini\antigravity\scratch\PCCOE_StudentName_PRN_123B1F001_AIML\Synopsis"
    out_file = os.path.join(out_dir, "Project_Synopsis_AUTOSAR_AI.pdf")
    generate_synopsis_pdf(out_file)
