import re
from typing import Dict, List, Set


class EntityExtractor:

    def __init__(self):

        self.entities = {

            #
            # Disorders
            #

            "depression": "disorder",
            "major depressive disorder": "disorder",
            "mdd": "disorder",
            "anxiety": "disorder",
            "generalized anxiety disorder": "disorder",
            "gad": "disorder",
            "ptsd": "disorder",
            "ocd": "disorder",
            "panic disorder": "disorder",
            "bipolar disorder": "disorder",
            "adhd": "disorder",
            "insomnia": "symptom",

            #
            # Therapies
            #

            "cbt": "therapy",
            "cognitive behavioral therapy": "therapy",
            "dbt": "therapy",
            "dialectical behavior therapy": "therapy",
            "behavioral activation": "therapy",
            "mindfulness": "therapy",

            #
            # Medication
            #

            "ssri": "medication",
            "snri": "medication",
            "sertraline": "medication",
            "fluoxetine": "medication",
            "escitalopram": "medication",

            #
            # Assessments
            #

            "phq-9": "assessment",
            "gad-7": "assessment",

            #
            # Symptoms
            #

            "fatigue": "symptom",
            "hopelessness": "symptom",
            "worthlessness": "symptom",
            "sleep": "symptom",
            "sadness": "symptom",
            "suicidal ideation": "symptom",
        }

    def extract(
        self,
        text: str,
    ) -> List[Dict]:

        text = text.lower()

        found = []

        for entity, entity_type in self.entities.items():

            pattern = r"\b" + re.escape(entity) + r"\b"

            if re.search(pattern, text):

                found.append({

                    "entity": entity,

                    "type": entity_type,

                })

        return found