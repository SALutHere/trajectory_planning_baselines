import heapq
import time

from algorithms.base import Planner
from core.registry import register_planner


@register_planner
class ThetaStar(Planner):
    name = "ThetaStar"

    def plan(self, grid, start, goal):
        t0 = time.perf_counter()

        g = {start: 0.0}
        parent = {start: None}

        openpq = []
        heapq.heappush(openpq, (grid.heuristic(start, goal), start))
        closed = set()

        while openpq:
            _, s = heapq.heappop(openpq)

            if s in closed:
                continue
            closed.add(s)

            if s == goal:
                path = self._reconstruct(parent, goal)
                return {
                    "path": path,
                    "time_ms": (time.perf_counter() - t0) * 1000,
                    "meta": {}
                }

            for s2 in grid.neighbors(s):
                # parent of s — p
                p = parent[s] if parent[s] is not None else s

                # Try LOS via p → s2
                if parent[s] is not None and grid.line_of_sight(p, s2):
                    new_g = g[p] + grid.heuristic(p, s2)
                    if new_g < g.get(s2, float("inf")):
                        g[s2] = new_g
                        parent[s2] = p
                        f = new_g + grid.heuristic(s2, goal)
                        heapq.heappush(openpq, (f, s2))

                else:
                    new_g = g[s] + grid.heuristic(s, s2)
                    if new_g < g.get(s2, float("inf")):
                        g[s2] = new_g
                        parent[s2] = s
                        f = new_g + grid.heuristic(s2, goal)
                        heapq.heappush(openpq, (f, s2))

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
