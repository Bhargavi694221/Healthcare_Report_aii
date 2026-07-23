from crewai import Agent
from utils.helpers import get_llm


def create_medical_history():
    return Agent(
        role="Medical History Analyst",
        goal="Summarize the patient's historical medical condition.",
        backstory="""
        You specialize in analyzing previous diagnoses,
        chronic illnesses, surgeries, medications,
        allergies, and treatment history.
        """,
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )