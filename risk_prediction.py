from crewai import Agent
from utils.helpers import get_llm


def create_risk_prediction():
    return Agent(
        role="Medical Risk Predictor",
        goal="Predict future health risks from patient data.",
        backstory="""
        You are a preventive healthcare specialist.
        Predict risks such as diabetes progression,
        heart disease, hypertension,
        kidney disease and other complications.
        """,
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )