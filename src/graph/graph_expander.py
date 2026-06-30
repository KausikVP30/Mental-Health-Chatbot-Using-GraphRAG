from typing import List


class GraphExpander:

    def expand(
        self,
        graphs,
        entities,
    ) -> List[str]:

        expanded = set()

        for graph in graphs:

            for entity in entities:

                expanded.add(entity)

                neighbors = graph.get_neighbors(entity)

                for n in neighbors:

                    expanded.add(n)

        return list(expanded)