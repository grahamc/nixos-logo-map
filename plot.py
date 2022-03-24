#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p python3 python3.pkgs.matplotlib

import matplotlib.pyplot as plt
import json

xs = []
ys = []
datas = []

with open("./combined.json") as f:
    data = json.loads(f.read())

fig, ax = plt.subplots()

for led in data:
    ax.scatter(led['x'], led['y'], marker=f"${led['led']}$", data=datas)


ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
plt.savefig('./plot.svg')
print("saved")