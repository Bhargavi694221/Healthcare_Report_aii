from crewai import Task
from agents.report_generator import create_report_generator


def create_report_task(
    document_task,
    history_task,
    comparison_task,
    risk_task,
    recommendation_task
):
    return Task(
        description="""
Generate a professional hospital report.

The report must contain:

1. Patient Details
2. Medical History
3. Current Health Status
4. Health Comparison
5. Risk Assessment
6. Clinical Recommendations
7. Overall Conclusion

The report should be suitable for hospital documentation.
""",
        expected_output="Final professional patient health report.",
        agent=create_report_generator(),
        context=[
            document_task,
            history_task,
            comparison_task,
            risk_task,
            recommendation_task
        ]
    )