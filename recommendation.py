from crewai import Agent
from utils.helpers import get_llm


def create_recommendation():
    return Agent(
        role="Clinical Recommendation Specialist",
        goal="Provide personalized clinical recommendations.",
        backstory="""
        You generate evidence-based recommendations
        regarding medication adherence, diet,
        exercise, follow-up testing,
        and lifestyle improvements.
        """,
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )