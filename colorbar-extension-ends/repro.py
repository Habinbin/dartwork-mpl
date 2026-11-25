"""Colorbar extension ends: matplotlib's triangles vs rectangles.

Usage: python repro.py OUT_STEM
Runs on dartwork-mpl 0.10.x (dm.check) and 0.7.x (dm.validate_figure).
"""

import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import dartwork_mpl as dm

out = sys.argv[1]

x = np.linspace(0.0, 1.0, 80)
X, Y = np.meshgrid(x, x)
Z = 2.0 + 1.5 * np.sin(3 * X) * np.cos(2 * Y) + 0.8 * X
levels = np.linspace(1.0, 3.5, 11)  # fixed levels: Z runs past both ends

with dm.style.context("scientific"):
    fig, axes = plt.subplots(1, 2, figsize=dm.figsize("17cm", "7cm"))
    for ax, rect in zip(axes, (False, True)):
        cs = ax.contourf(X, Y, Z, levels=levels, cmap="dc.blue", extend="both")
        fig.colorbar(cs, ax=ax, label="Value [-]", extendrect=rect)
        ax.set(xlabel="x [-]", ylabel="y [-]")
        ax.set_title(
            "extend=\"both\": triangles (default)" if not rect else "extendrect=True: rectangles"
        )
    dm.simple_layout(fig)
    if hasattr(dm, "check"):
        print(dm.check(fig))
    else:
        print(dm.validate_figure(fig))
    dm.save_formats(fig, out, formats=("png",))
    plt.close(fig)
