import argparse
import algorithms
import scenarios

from core.registry import SCENARIOS
from core.experiment import run_multiple_and_save
from core.utils import reset_output


def make_scenario(cls, **kwargs):
    return cls(**kwargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--width", type=int, default=None)
    parser.add_argument("--height", type=int, default=None)
    parser.add_argument("--obstacle_prob", type=float, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--runs", type=int, default=10)

    args = parser.parse_args()

    reset_output()

    kwargs = {}
    for key in ["width", "height", "obstacle_prob", "seed"]:
        val = getattr(args, key)
        if val is not None:
            kwargs[key] = val

    for scenario_name, scenario_obj in SCENARIOS.items():
        print(f"\n=== Scenario: {scenario_name} ===")

        cls = scenario_obj.__class__
        SCENARIOS[scenario_name] = make_scenario(cls, **kwargs)

        run_multiple_and_save(scenario_name, runs=args.runs)

    print("\n✅ Completed run_all")
