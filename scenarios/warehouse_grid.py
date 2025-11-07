import random
from scenarios.base import Scenario
from core.grid import Grid
from core.registry import register_scenario


@register_scenario
class WarehouseScenario(Scenario):
    name = "warehouse_grid"

    def __init__(self, width=50, height=50, block_w=4, block_h=10, spacing=3, seed=None):
        self.width = width
        self.height = height
        self.block_w = block_w
        self.block_h = block_h
        self.spacing = spacing
        self.seed = seed

    def generate(self):
        if self.seed is not None:
            random.seed(self.seed)

        W, H = self.width, self.height
        grid = [[0 for _ in range(W)] for _ in range(H)]

        y = self.spacing
        while y + self.block_h < H:
            x = self.spacing
            while x + self.block_w < W:
                for yy in range(y, y + self.block_h):
                    for xx in range(x, x + self.block_w):
                        grid[yy][xx] = 1
                x += self.block_w + self.spacing
            y += self.block_h + self.spacing

        start = (1, 1)
        goal = (W - 2, H - 2)

        grid[start[1]][start[0]] = 0
        grid[goal[1]][goal[0]] = 0

        return Grid(grid), start, goal
