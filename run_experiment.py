import algorithms
import scenarios

from core.experiment import run_once
from visualize.plot import save_run_visuals

if __name__ == "__main__":
    # r = run_once("random_grid")
    r = run_once("maze_grid")

    print("Start:", r["start"])
    print("Goal:", r["goal"])

    for algo, res in r["results"].items():
        print(f"\n=== {algo} ===")
        print("time_ms:", res["time_ms"])
        print("path found:", res["path"] is not None)
        if res["path"]:
            print("path length:", len(res["path"]))

    save_run_visuals(
        r["grid"], r["start"], r["goal"],
        r["results"], run_id=0, outdir="output/runs"
    )
