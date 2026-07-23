import os
import streamlit as st

from tools.pdf_reader import PDFReader
from tools.pdf_export import PDFExporter
from crew.run_crew import run_pipeline

st.set_page_config(
    page_title="AI Healthcare Report Generator",
    layout="wide"
)

st.title("🏥 Agentic AI Healthcare Report Generator")
st.write("Upload previous and current patient reports to generate an AI-powered healthcare report.")

# ---------------- Upload Files ----------------

old_file = st.file_uploader(
    "Upload Previous Patient Report",
    type=["pdf"],
    key="old"
)

new_file = st.file_uploader(
    "Upload Current Patient Report",
    type=["pdf"],
    key="new"
)

if old_file and new_file:

    os.makedirs("uploads", exist_ok=True)

    old_path = os.path.join("uploads", "old_report.pdf")
    new_path = os.path.join("uploads", "new_report.pdf")

    with open(old_path, "wb") as f:
        f.write(old_file.getbuffer())

    with open(new_path, "wb") as f:
        f.write(new_file.getbuffer())

    st.success("PDFs uploaded successfully.")

    # ---------------- Read PDFs ----------------

    with st.spinner("Reading PDF reports..."):

        old_text = PDFReader.read_pdf(old_path)
        new_text = PDFReader.read_pdf(new_path)

    # ---------------- Run CrewAI ----------------

    with st.spinner("Running AI Healthcare Agents..."):

        result = run_pipeline(
            old_report=old_text,
            new_report=new_text
        )

    # ---------------- Display Report ----------------

    report_text = result.raw if hasattr(result, "raw") else str(result)

    st.subheader("📄 AI Generated Healthcare Report")

    st.text_area(
        "Report",
        report_text,
        height=500
    )

    # ---------------- Export PDF ----------------

    pdf_path = PDFExporter.export(
        report_text=report_text,
        patient_name="patient"
    )

    st.success("Report generated successfully!")

    with open(pdf_path, "rb") as pdf:

        st.download_button(
            label="📥 Download PDF Report",
            data=pdf,
            file_name=os.path.basename(pdf_path),
            mime="application/pdf"
        )