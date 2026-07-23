
from tools.compare_tool import CompareTool

old_data = {
    "blood_pressure": "150/95",
    "heart_rate": "92",
    "blood_sugar": "180",
    "hba1c": "8.5",
    "cholesterol": "240",
    "weight": "84",
    "diagnosis": [
        "Type 2 Diabetes",
        "Hypertension"
    ],
    "medications": [
        "Metformin",
        "Amlodipine"
    ]
}

new_data = {
    "blood_pressure": "128/82",
    "heart_rate": "76",
    "blood_sugar": "118",
    "hba1c": "6.8",
    "cholesterol": "185",
    "weight": "79",
    "diagnosis": [
        "Type 2 Diabetes (Improved)",
        "Hypertension (Controlled)"
    ],
    "medications": [
        "Metformin",
        "Amlodipine"
    ]
}

comparison = CompareTool.compare(old_data, new_data)

print(comparison)