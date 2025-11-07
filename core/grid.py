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

    def line_of_sight(self, a, b):
        """
        Проверка прямой видимости между двумя клетками a и b.
        Возвращает True, если путь свободен (нет препятствий).
        Используем алгоритм Брезенхэма.
        """
        (x0, y0) = a
        (x1, y1) = b

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        sx = 1 if x1 >= x0 else -1
        sy = 1 if y1 >= y0 else -1

        err = dx - dy

        x, y = x0, y0

        while True:
            if not self.passable((x, y)):
                return False
            if (x, y) == (x1, y1):
                break

            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

        return True

    @staticmethod
    def heuristic(a,b):
        (x1,y1),(x2,y2) = a,b
        return ((x1-x2)**2 + (y1-y2)**2) ** 0.5
