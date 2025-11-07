import random
from scenarios.base import Scenario
from core.grid import Grid
from core.registry import register_scenario

@register_scenario
class RandomGridScenario(Scenario):
    name = "random_grid"

    def __init__(self, width=40, height=40, obstacle_prob=0.25, seed=None):
        self.width = width
        self.height = height
        self.obstacle_prob = obstacle_prob
        self.seed = seed

    def generate(self):
        if self.seed is not None:
            random.seed(self.seed)

        grid = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                # 1 = obstacle, 0 = free
                row.append(1 if random.random() < self.obstacle_prob else 0)
            grid.append(row)

        start = (0, 0)
        goal = (self.width - 1, self.height - 1)

        grid[start[1]][start[0]] = 0
        grid[goal[1]][goal[0]] = 0

        return Grid(grid), start, goal
