import algorithms
import scenarios

from core.experiment import run_and_save

if __name__ == "__main__":
    scenario = "random_grid"
    run_id = 0

    r = run_and_save(scenario, run_id)

    print("Start:", r["start"])
    print("Goal:", r["goal"])

    for algo, res in r["results"].items():
        print(f"\n=== {algo} ===")
        print("time_ms:", res["time_ms"])
        print("path found:", res["path"] is not None)
        if res["path"]:
            print("path length:", len(res["path"]))
