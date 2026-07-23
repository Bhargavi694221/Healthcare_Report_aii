from crewai import Task
from agents.risk_prediction import create_risk_prediction


def create_risk_task(history_task, comparison_task):
    return Task(
        description="""
Using the patient's history and comparison,
predict future medical risks.

Include:

- Diabetes Risk
- Hypertension Risk
- Heart Disease Risk
- Kidney Disease Risk
- Stroke Risk

Explain each risk level.
""",
        expected_output="Comprehensive risk assessment.",
        agent=create_risk_prediction(),
        context=[history_task, comparison_task]
    )