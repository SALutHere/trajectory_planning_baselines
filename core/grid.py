class Grid:
    def __init__(self, grid, eight_connected=True):
        self.grid = grid
        self.H = len(grid)
        self.W = len(grid[0]) if self.H else 0
        self.eight = eight_connected

    def in_bounds(self, p):
        x,y = p
        return 0 <= x < self.W and 0 <= y < self.H

    def passable(self, p):
        x,y = p
        return self.grid[y][x] == 0

    def neighbors(self, p):
        x,y = p
        dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
        dirs8 = dirs4 + [(1,1),(1,-1),(-1,1),(-1,-1)]
        dirs = dirs8 if self.eight else dirs4
        for dx,dy in dirs:
            q = (x+dx, y+dy)
            if self.in_bounds(q) and self.passable(q):
                yield q

    @staticmethod
    def heuristic(a,b):
        (x1,y1),(x2,y2) = a,b
        return ((x1-x2)**2 + (y1-y2)**2) ** 0.5
