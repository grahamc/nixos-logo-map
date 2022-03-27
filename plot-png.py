#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p python3 python3.pkgs.matplotlib

import matplotlib.pyplot as plt
import json
import sys

color = sys.argv[1]

with open(f"./combined-{color}.json") as f:
    data = json.loads(f.read())

fig, ax = plt.subplots()

for led in data:
    ax.scatter(led['x'], led['y'], marker=f"${led['led']}$")

ax.imshow(plt.imread("./locator.png"))
ax.set_xlim(600, 1600)
ax.set_ylim(1000, 100)


ax.set_xlim(600, 750)
ax.set_ylim(650, 500)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
plt.savefig(f"./plot-{color}.png")
print("saved")
