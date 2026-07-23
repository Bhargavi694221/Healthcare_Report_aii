import datetime
from utils.helpers import get_llm


class ReportWriter:
    """
    Uses LLM + structured data to generate a professional medical report.
    """

    @staticmethod
    def generate(final_data: dict) -> str:
        """
        final_data = {
            "document": {...},
            "history": "...",
            "comparison": "...",
            "risk": "...",
            "recommendation": "..."
        }
        """

        llm = get_llm()

        document = final_data.get("document", {})
        history = final_data.get("history", "")
        comparison = final_data.get("comparison", "")
        risk = final_data.get("risk", "")
        recommendation = final_data.get("recommendation", "")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ---------------- PROMPT TO LLM ----------------
        prompt = f"""
You are a senior hospital medical report generator AI.

Create a PROFESSIONAL, STRUCTURED, CLINICAL-QUALITY PATIENT REPORT.

Use the data below:

PATIENT DETAILS:
{document}

MEDICAL HISTORY:
{history}

COMPARISON (OLD vs CURRENT):
{comparison}

RISK ANALYSIS:
{risk}

RECOMMENDATIONS:
{recommendation}

RULES:
- Use formal medical language
- Keep structure clean and hospital-grade
- Do NOT hallucinate new medical facts
- Organize into sections:
  1. Patient Details
  2. Current Health Status
  3. Medical History Summary
  4. Comparative Analysis
  5. Risk Assessment
  6. Recommendations
  7. Final Conclusion

Add timestamp: {timestamp}
"""

        # ---------------- CALL LLM ----------------
        response = llm.call(prompt)

        # ---------------- RETURN FINAL REPORT ----------------
        return response