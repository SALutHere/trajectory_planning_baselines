from core.registry import PLANNERS, SCENARIOS

def run_once(scenario_name):
    """
    Выполняет 1 прогон сценария
    для всех зарегистрированных алгоритмов.
    Возвращает структуру:
    {
        "grid": Grid,
        "start": (x,y),
        "goal": (x,y),
        "results": {
            planner_name: { "path", "time_ms", "meta" }
        }
    }
    """
    if scenario_name not in SCENARIOS:
        raise ValueError(f"Unknown scenario: {scenario_name}")

    scenario = SCENARIOS[scenario_name]
    grid, start, goal = scenario.generate()

    out = {
        "grid": grid,
        "start": start,
        "goal": goal,
        "results": {}
    }

    for name, planner in PLANNERS.items():
        res = planner.plan(grid, start, goal)
        out["results"][name] = res

    return out


def run_multiple(scenario_name, runs=5):
    return [run_once(scenario_name) for _ in range(runs)]
