import heapq
import time

from algorithms.base import Planner
from core.registry import register_planner

@register_planner
class AStar(Planner):
    name = "AStar"

    def plan(self, grid, start, goal):
        """
        Поиск пути алгоритмом A*
        """
        t0 = time.perf_counter()

        open_set = []
        heapq.heappush(open_set, (0, start))
        came = {start: None}
        g = {start: 0}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = self._reconstruct(came, current)
                return {
                    "path": path,
                    "time_ms": (time.perf_counter() - t0) * 1000,
                    "meta": {}
                }

            for nxt in grid.neighbors(current):
                tentative_g = g[current] + grid.heuristic(current, nxt)
                if tentative_g < g.get(nxt, float("inf")):
                    g[nxt] = tentative_g
                    came[nxt] = current
                    f = tentative_g + grid.heuristic(nxt, goal)
                    heapq.heappush(open_set, (f, nxt))

        return {
            "path": None,
            "time_ms": (time.perf_counter() - t0) * 1000,
            "meta": {}
        }

    def _reconstruct(self, came, node):
        path = []
        while node is not None:
            path.append(node)
            node = came[node]
        return list(reversed(path))
