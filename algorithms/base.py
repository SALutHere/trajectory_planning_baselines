class Planner:
    name = "BasePlanner"

    def plan(self, grid, start, goal):
        """
        MUST return dict:
        {
            "path": [(x,y), ...] or None,
            "time_ms": float,
            "meta": dict
        }
        """
        raise NotImplementedError
