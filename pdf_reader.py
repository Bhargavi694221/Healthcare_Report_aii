
"""
PDF Reader Tool

Reads one or multiple PDF reports
and extracts all text.
"""

import pdfplumber
import os


class PDFReader:

    @staticmethod
    def read_pdf(pdf_path: str) -> str:
        """
        Read a PDF file and return extracted text.
        """

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"{pdf_path} not found.")

        text = ""

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    @staticmethod
    def read_multiple(pdf_paths: list):
        """
        Read multiple PDFs.
        """

        documents = {}

        for file in pdf_paths:
            try:
                documents[file] = PDFReader.read_pdf(file)
            except Exception as e:
                documents[file] = f"Error: {e}"

        return documents
