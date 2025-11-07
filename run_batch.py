import algorithms
import scenarios

from core.experiment import run_multiple_and_save

if __name__ == "__main__":
    scenario = "random_grid"
    runs = 10

    run_multiple_and_save(scenario, runs)
