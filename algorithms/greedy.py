import heapq
import time

from algorithms.base import Planner
from core.registry import register_planner


@register_planner
class GreedyBestFirst(Planner):
    name = "Greedy"

    def plan(self, grid, start, goal):
        t0 = time.perf_counter()

        openpq = []
        heapq.heappush(openpq, (grid.heuristic(start, goal), start))
        parent = {start: None}
        visited = set()

        while openpq:
            _, current = heapq.heappop(openpq)

            if current in visited:
                continue
            visited.add(current)

            if current == goal:
                path = self._reconstruct(parent, goal)
                return {
                    "path": path,
                    "time_ms": (time.perf_counter() - t0) * 1000,
                    "meta": {}
                }

            for nxt in grid.neighbors(current):
                if nxt not in visited:
                    parent.setdefault(nxt, current)
                    heapq.heappush(
                        openpq,
                        (grid.heuristic(nxt, goal), nxt)
                    )

        return {
            "path": None,
            "time_ms": (time.perf_counter() - t0) * 1000,
            "meta": {}
        }

    def _reconstruct(self, parent, node):
        path = []
        while node is not None:
            path.append(node)
            node = parent[node]
        return list(reversed(path))
