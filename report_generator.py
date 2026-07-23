from crewai import Agent
from utils.helpers import get_llm


def create_report_generator():
    return Agent(
        role="Hospital Medical Report Writer",
        goal="Generate a professional hospital-style patient report.",
        backstory="""
        You prepare clear, concise, and structured medical reports
        suitable for doctors, hospitals, and patients.
        The report must summarize patient history,
        current condition, health comparison,
        identified risks, and recommendations.
        """,
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )