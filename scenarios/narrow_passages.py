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

        main_x = W // 2
        for y in range(H):
            grid[y][main_x] = 0

        ys = sorted(random.sample(range(2, H-2), self.corridors))
        for y in ys:
            for x in range(W):
                grid[y][x] = 0
            grid[y][main_x] = 0

        start_y = ys[0]
        goal_y  = ys[-1]

        start = (1, start_y)
        goal  = (W - 2, goal_y)

        grid[start_y][1] = 0
        grid[goal_y][W - 2] = 0

        return Grid(grid), start, goal

