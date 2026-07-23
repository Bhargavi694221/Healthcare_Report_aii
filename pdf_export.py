import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class PDFExporter:
    """
    Converts final medical report text into a structured PDF file.
    """

    @staticmethod
    def export(report_text: str, patient_name: str = "patient") -> str:
        """
        Saves report as PDF and returns file path.
        """

        # Ensure reports directory exists
        os.makedirs("reports", exist_ok=True)

        # Clean filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{patient_name.replace(' ', '_')}_{timestamp}.pdf"
        file_path = os.path.join("reports", filename)

        # Create PDF
        pdf = canvas.Canvas(file_path, pagesize=A4)
        width, height = A4

        # Header
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, height - 50, "PATIENT HEALTHCARE REPORT")

        pdf.setFont("Helvetica", 10)
        pdf.drawString(50, height - 70, f"Generated: {timestamp}")

        # Body text
        y = height - 100
        lines = report_text.split("\n")

        pdf.setFont("Helvetica", 9)

        for line in lines:
            if y < 50:
                pdf.showPage()
                pdf.setFont("Helvetica", 9)
                y = height - 50

            pdf.drawString(50, y, line[:120])  # prevent overflow
            y -= 12

        pdf.save()

        return file_path