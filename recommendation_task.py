from crewai import Task
from agents.recommendation import create_recommendation


def create_recommendation_task(risk_task):
    return Task(
        description="""
Generate personalized medical recommendations.

Include:

- Diet
- Exercise
- Lifestyle improvements
- Medication adherence
- Follow-up schedule
- Suggested medical tests
""",
        expected_output="Clinical recommendations.",
        agent=create_recommendation(),
        context=[risk_task]
    )