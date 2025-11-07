PLANNERS = {}
SCENARIOS = {}

def register_planner(cls):
    PLANNERS[cls.name] = cls()
    return cls

def register_scenario(cls):
    SCENARIOS[cls.name] = cls()
    return cls
