from crewai import Task
from agents.document_reader import create_document_reader


def create_document_task(old_report: str, new_report: str):
    return Task(
        description=f"""
You are given two patient medical reports.

Previous Report:
{old_report}

Current Report:
{new_report}

Extract the following information from BOTH reports:

- Patient Name
- Age
- Gender
- Visit Date
- Blood Pressure
- Heart Rate
- Blood Sugar
- HbA1c
- Cholesterol
- Weight
- Diagnosis
- Medications
- Doctor Notes

Return the result in structured JSON.
""",
        expected_output="Structured JSON containing extracted patient information.",
        agent=create_document_reader()
    )