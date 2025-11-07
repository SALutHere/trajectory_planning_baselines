import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def _plot_grid(ax, grid):
    mask = np.array(grid.grid, dtype=np.uint8)
    ax.imshow(1 - mask, origin="lower", interpolation="none")
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-0.5, grid.W - 0.5)
    ax.set_ylim(-0.5, grid.H - 0.5)
    ax.set_xticks([])
    ax.set_yticks([])

def _plot_path(ax, path):
    if not path:
        return
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]
    ax.plot(xs, ys, linewidth=2)

def _plot_points(ax, start, goal):
    ax.scatter([start[0]], [start[1]])
    ax.scatter([goal[0]], [goal[1]])

def save_single(grid, start, goal, path, savepath, title=None):
    os.makedirs(os.path.dirname(savepath), exist_ok=True)
    fig = plt.figure(figsize=(6, 6))
    ax = plt.gca()
    _plot_grid(ax, grid)
    _plot_path(ax, path)
    _plot_points(ax, start, goal)
    if title:
        ax.set_title(title)
    plt.savefig(savepath, bbox_inches="tight")
    plt.close(fig)

def save_overlay(grid, start, goal, name_to_path, savepath, title=None):
    os.makedirs(os.path.dirname(savepath), exist_ok=True)
    fig = plt.figure(figsize=(6, 6))
    ax = plt.gca()
    _plot_grid(ax, grid)
    for _, path in name_to_path.items():
        _plot_path(ax, path)
    _plot_points(ax, start, goal)
    if title:
        ax.set_title(title)
    plt.savefig(savepath, bbox_inches="tight")
    plt.close(fig)

def save_run_visuals(grid, start, goal, results: dict, run_id: int, outdir="output/runs"):
    """
    results: { planner_name: {"path": [...], "time_ms": float, "meta": {...}}, ... }
    """
    run_dir = os.path.join(outdir, f"run_{run_id}")
    os.makedirs(run_dir, exist_ok=True)

    for name, res in results.items():
        save_single(
            grid, start, goal,
            res.get("path"),
            savepath=os.path.join(run_dir, f"{name}.png"),
            title=f"{name} | run {run_id}"
        )

    name_to_path = {name: res.get("path") for name, res in results.items()}
    save_overlay(
        grid, start, goal, name_to_path,
        savepath=os.path.join(run_dir, "all.png"),
        title=f"ALL | run {run_id}"
    )
