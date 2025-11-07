import argparse
import algorithms
import scenarios

from core.registry import SCENARIOS
from core.experiment import run_multiple_and_save


def make_scenario(name, **kwargs):
    cls = SCENARIOS[name].__class__
    return cls(**kwargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("scenario", type=str)
    parser.add_argument("--width", type=int, default=None)
    parser.add_argument("--height", type=int, default=None)
    parser.add_argument("--obstacle_prob", type=float, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--runs", type=int, default=10)

    args = parser.parse_args()

    kwargs = {}
    for key in ["width", "height", "obstacle_prob", "seed"]:
        val = getattr(args, key)
        if val is not None:
            kwargs[key] = val

    scenario = make_scenario(args.scenario, **kwargs)
    SCENARIOS[args.scenario] = scenario

    run_multiple_and_save(args.scenario, args.runs)
    print("\n✅ Batch completed")
