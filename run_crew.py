from crew.crew import HospitalReportCrew


def run_pipeline(old_report: str, new_report: str):
    """
    Runs the complete healthcare CrewAI pipeline.
    """

    hospital_crew = HospitalReportCrew(
        old_report=old_report,
        new_report=new_report,
    )

    result = hospital_crew.run()

    return result


# ----------------------------------
# Standalone Test
# ----------------------------------

if __name__ == "__main__":

    old_report = """
    Patient Name: John Smith
    Age: 52
    Blood Pressure: 150/95
    Blood Sugar: 180
    HbA1c: 8.5%
    Diagnosis:
    Diabetes
    Hypertension
    """

    new_report = """
    Patient Name: John Smith
    Age: 52
    Blood Pressure: 128/82
    Blood Sugar: 135
    HbA1c: 7.1%
    Diagnosis:
    Diabetes
    """

    result = run_pipeline(
        old_report,
        new_report
    )

    if hasattr(result, "raw"):
        print(result.raw)
    else:
        print(result)