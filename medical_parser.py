
import json
from utils.helpers import ask_llm


class MedicalParser:

    @staticmethod
    def parse(report_text: str):
        prompt = f"""
You are an expert medical report parser.

Extract the following information from the patient report.

Return ONLY valid JSON.

Required fields:

{{
  "patient_name":"",
  "age":"",
  "gender":"",
  "visit_date":"",
  "blood_pressure":"",
  "heart_rate":"",
  "blood_sugar":"",
  "hba1c":"",
  "cholesterol":"",
  "weight":"",
  "diagnosis":[],
  "medications":[],
  "doctor_notes":""
}}

Patient Report:

{report_text}
"""

        response = ask_llm(prompt)

        try:
            return json.loads(response)
        except Exception:
            return {
                "raw_response": response
            }
