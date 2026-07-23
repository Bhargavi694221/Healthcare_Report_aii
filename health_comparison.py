from crewai import Agent
from utils.helpers import get_llm


def create_health_comparison():
    return Agent(
        role="Health Comparison Specialist",
        goal="Compare previous and latest medical reports.",
        backstory="""
        You are a senior physician specializing in identifying
        improvements, deteriorations, stable parameters,
        and significant clinical changes.
        """,
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )