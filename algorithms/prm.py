import random
import time
import heapq

from algorithms.base import Planner
from core.registry import register_planner


@register_planner
class PRM(Planner):
    name = "PRM"

    def __init__(self, n_samples=200, k=10):
        self.n_samples = n_samples
        self.k = k

    def plan(self, grid, start, goal):
        t0 = time.perf_counter()

        if not grid.passable(start) or not grid.passable(goal):
            return {
                "path": None,
                "time_ms": 0.0,
                "meta": {}
            }

        pts = [start, goal]
        while len(pts) < self.n_samples:
            p = (
                random.randint(0, grid.W - 1),
                random.randint(0, grid.H - 1)
            )
            if grid.passable(p):
                pts.append(p)

        adj = {p: [] for p in pts}

        for i, p in enumerate(pts):
            dlist = sorted(
                pts,
                key=lambda q: grid.heuristic(p, q)
            )
            for q in dlist[1:self.k + 1]:
                if grid.line_of_sight(p, q):
                    adj[p].append(q)
                    adj[q].append(p)

        path = self.graph_astar(adj, start, goal, grid)

        return {
            "path": path,
            "time_ms": (time.perf_counter() - t0) * 1000,
            "meta": {
                "samples": len(pts)
            }
        }

    def graph_astar(self, adj, start, goal, grid):
        g = {start: 0.0}
        parent = {start: None}

        openpq = []
        heapq.heappush(openpq, (grid.heuristic(start, goal), start))
        visited = set()

        while openpq:
            _, u = heapq.heappop(openpq)

            if u in visited:
                continue
            visited.add(u)

            if u == goal:
                return self._reconstruct(parent, goal)

            for v in adj[u]:
                nd = g[u] + grid.heuristic(u, v)

                if nd < g.get(v, float("inf")):
                    g[v] = nd
                    parent[v] = u
                    f = nd + grid.heuristic(v, goal)
                    heapq.heappush(openpq, (f, v))

        return None

    def _reconstruct(self, parent, node):
        path = []
        while node is not None:
            path.append(node)
            node = parent[node]
        return list(reversed(path))
