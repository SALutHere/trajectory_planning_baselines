import algorithms
import scenarios

from core.registry import SCENARIOS
from core.experiment import run_multiple_and_save

if __name__ == "__main__":
    runs = 10
    for scenario_name in SCENARIOS.keys():
        print(f"\n=== Scenario: {scenario_name} ===")
        run_multiple_and_save(scenario_name, runs=runs)
