# core/experiment.py
import csv
import os
from core.registry import PLANNERS, SCENARIOS
from visualize.plot import save_run_visuals


def run_once(scenario_name):
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


def _save_csv_row(row, scenario_name, outdir="output"):
    scenario_dir = os.path.join(outdir, scenario_name)
    os.makedirs(scenario_dir, exist_ok=True)

    csv_path = os.path.join(scenario_dir, f"{scenario_name}.csv")
    file_exists = os.path.exists(csv_path)

    fieldnames = [
        "run_id", "scenario", "algorithm",
        "time_ms", "success", "path_len",
        "start_x", "start_y", "goal_x", "goal_y"
    ]

    with open(csv_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def run_and_save(scenario_name, run_id, outdir="output"):
    r = run_once(scenario_name)

    scenario_dir = os.path.join(outdir, scenario_name)
    os.makedirs(scenario_dir, exist_ok=True)

    save_run_visuals(
        r["grid"], r["start"], r["goal"],
        r["results"],
        run_id=run_id,
        outdir=scenario_dir
    )

    for algo, res in r["results"].items():
        row = {
            "run_id": run_id,
            "scenario": scenario_name,
            "algorithm": algo,
            "time_ms": res["time_ms"],
            "success": res["path"] is not None,
            "path_len": len(res["path"]) if res["path"] else None,
            "start_x": r["start"][0],
            "start_y": r["start"][1],
            "goal_x": r["goal"][0],
            "goal_y": r["goal"][1],
        }
        _save_csv_row(row, scenario_name, outdir)

    return r


def run_multiple_and_save(scenario_name, runs=10, outdir="output"):
    for i in range(runs):
        run_and_save(scenario_name, i, outdir)
