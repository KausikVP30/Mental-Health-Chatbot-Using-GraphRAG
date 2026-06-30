from itertools import combinations


class RelationExtractor:

    def extract(self, entities):

        relations = []

        for e1, e2 in combinations(entities, 2):

            relations.append({

                "source": e1["entity"],

                "target": e2["entity"],

                "relation": "related_to",

                "weight": 1.0,

            })

        return relations
