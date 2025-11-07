import random
from scenarios.base import Scenario
from core.grid import Grid
from core.registry import register_scenario


@register_scenario
class MazeGridScenario(Scenario):
    name = "maze_grid"

    def __init__(self, width=41, height=41, seed=None):
        self.width = width if width % 2 == 1 else width + 1
        self.height = height if height % 2 == 1 else height + 1
        self.seed = seed

    def generate(self):
        if self.seed is not None:
            random.seed(self.seed)

        W, H = self.width, self.height

        grid = [[1 for _ in range(W)] for _ in range(H)]

        def carve(x, y):
            grid[y][x] = 0
            dirs = [(2, 0), (-2, 0), (0, 2), (0, -2)]
            random.shuffle(dirs)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 < nx < W and 0 < ny < H and grid[ny][nx] == 1:
                    grid[y + dy // 2][x + dx // 2] = 0
                    carve(nx, ny)

        carve(1, 1)

        start = (1, 1)
        goal = (W - 2, H - 2)
        grid[start[1]][start[0]] = 0
        grid[goal[1]][goal[0]] = 0

        return Grid(grid), start, goal
