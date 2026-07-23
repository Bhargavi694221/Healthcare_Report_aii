from crewai import Task
from agents.medical_history import create_medical_history


def create_history_task(document_task):
    return Task(
        description="""
Analyze the extracted patient information.

Create a complete medical history including:

- Chronic diseases
- Previous diagnoses
- Medication history
- Allergies
- Previous treatments
- Lifestyle observations
""",
        expected_output="Detailed patient medical history.",
        agent=create_medical_history(),
        context=[document_task]
    )