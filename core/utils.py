import shutil
import os

def reset_output(outdir="output"):
    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir, exist_ok=True)
