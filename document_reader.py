from crewai import Agent
from utils.helpers import get_llm


def create_document_reader():
    return Agent(
        role="Medical Document Reader",
        goal="Extract complete patient medical information from uploaded medical reports.",
        backstory="""
        You are an experienced hospital medical records specialist.
        You accurately extract patient demographics, vital signs,
        diagnoses, medications, laboratory values, and doctor's notes
        from medical reports.
        """,
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )