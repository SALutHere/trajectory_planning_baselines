import heapq
import time

from algorithms.base import Planner
from core.registry import register_planner


@register_planner
class Dijkstra(Planner):
    name = "Dijkstra"

    def plan(self, grid, start, goal):
        t0 = time.perf_counter()

        dist = {start: 0.0}
        parent = {start: None}
        pq = [(0.0, start)]
        visited = set()

        while pq:
            d, u = heapq.heappop(pq)

            if u in visited:
                continue
            visited.add(u)

            if u == goal:
                path = self._reconstruct(parent, goal)
                return {
                    "path": path,
                    "time_ms": (time.perf_counter() - t0) * 1000,
                    "meta": {}
                }

            for v in grid.neighbors(u):
                nd = d + grid.heuristic(u, v)

                if nd < dist.get(v, float("inf")):
                    dist[v] = nd
                    parent[v] = u
                    heapq.heappush(pq, (nd, v))

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
