
class CompareTool:

    @staticmethod
    def compare(old_data: dict, new_data: dict):
        comparison = {}

        fields = [
            "blood_pressure",
            "heart_rate",
            "blood_sugar",
            "hba1c",
            "cholesterol",
            "weight"
        ]

        for field in fields:
            comparison[field] = {
                "previous": old_data.get(field, "N/A"),
                "current": new_data.get(field, "N/A")
            }

        comparison["old_diagnosis"] = old_data.get("diagnosis", [])
        comparison["new_diagnosis"] = new_data.get("diagnosis", [])

        comparison["old_medications"] = old_data.get("medications", [])
        comparison["new_medications"] = new_data.get("medications", [])

        return comparison
