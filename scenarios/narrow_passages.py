import random
from scenarios.base import Scenario
from core.grid import Grid
from core.registry import register_scenario


@register_scenario
class NarrowPassages(Scenario):
    name = "narrow_passages"

    def __init__(self, width=50, height=50, corridors=4, seed=None):
        self.width = width
        self.height = height
        self.corridors = corridors
        self.seed = seed

    def generate(self):
        if self.seed is not None:
            random.seed(self.seed)

        W, H = self.width, self.height
        grid = [[1 for _ in range(W)] for _ in range(H)]

        for i in range(self.corridors):
            y = random.randint(1, H - 2)
            for x in range(W):
                grid[y][x] = 0

        for i in range(self.corridors - 1):
            y1 = random.randint(1, H - 2)
            x = random.randint(1, W - 2)
            for y in range(min(y1, y1 + 5), max(y1, y1 + 5)):
                if 0 <= y < H:
                    grid[y][x] = 0

        start = (1, 1)
        goal = (W - 2, H - 2)
        grid[start[1]][start[0]] = 0
        grid[goal[1]][goal[0]] = 0

        return Grid(grid), start, goal
