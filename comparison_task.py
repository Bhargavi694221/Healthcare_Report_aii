from crewai import Task
from agents.health_comparison import create_health_comparison


def create_comparison_task(document_task):
    return Task(
        description="""
Compare the old and current medical reports.

Identify:

- Improvements
- Worsening conditions
- Stable parameters
- Medication changes
- New diagnoses
- Laboratory changes

Provide a detailed comparison.
""",
        expected_output="Detailed health comparison.",
        agent=create_health_comparison(),
        context=[document_task]
    )