from crewai import Crew, Process

from tasks.document_task import create_document_task
from tasks.history_task import create_history_task
from tasks.comparison_task import create_comparison_task
from tasks.risk_task import create_risk_task
from tasks.recommendation_task import create_recommendation_task
from tasks.report_task import create_report_task


class HospitalReportCrew:

    def __init__(self, old_report: str, new_report: str):
        self.old_report = old_report
        self.new_report = new_report

    def build_crew(self):

        # ---------------- Document Extraction ----------------
        document_task = create_document_task(
            self.old_report,
            self.new_report
        )

        # ---------------- Medical History ----------------
        history_task = create_history_task(document_task)

        # ---------------- Comparison ----------------
        comparison_task = create_comparison_task(document_task)

        # ---------------- Risk Prediction ----------------
        risk_task = create_risk_task(
            history_task,
            comparison_task
        )

        # ---------------- Recommendation ----------------
        recommendation_task = create_recommendation_task(
            risk_task
        )

        # ---------------- Final Report ----------------
        report_task = create_report_task(
            document_task,
            history_task,
            comparison_task,
            risk_task,
            recommendation_task
        )

        crew = Crew(

            agents=[
                document_task.agent,
                history_task.agent,
                comparison_task.agent,
                risk_task.agent,
                recommendation_task.agent,
                report_task.agent
            ],

            tasks=[
                document_task,
                history_task,
                comparison_task,
                risk_task,
                recommendation_task,
                report_task
            ],

            process=Process.sequential,

            verbose=True
        )

        return crew

    def run(self):

        crew = self.build_crew()

        result = crew.kickoff()

        return result