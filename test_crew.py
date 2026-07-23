from crew.run_crew import run_pipeline

old_report = """
Patient Name: John Smith
Age: 52
Gender: Male
Blood Pressure: 150/95
Blood Sugar: 180
HbA1c: 8.5%
Diagnosis:
- Type 2 Diabetes
- Hypertension
"""

new_report = """
Patient Name: John Smith
Age: 52
Gender: Male
Blood Pressure: 128/82
Blood Sugar: 135
HbA1c: 7.1%
Diagnosis:
- Type 2 Diabetes
"""

result = run_pipeline(
    old_report=old_report,
    new_report=new_report
)

if hasattr(result, "raw"):
    print(result.raw)
else:
    print(result)