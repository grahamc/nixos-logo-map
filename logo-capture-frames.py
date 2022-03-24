#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p python3 ffmpeg curl

import subprocess
import sys

color = sys.argv[1]

for lednum in range(0, 360):
    print(f"Frame #{lednum}")
    colors = []
    for _ in range(0, 360):
        colors.append('000000')

    colors[lednum] = color

    subprocess.run(["rm", f"./led-{lednum}.bmp"], check=False)
    subprocess.run(["curl", "-v", "http://10.5.4.51:3030?message=" + (",".join(colors))], check=True)
    subprocess.run(["ffmpeg", "-f", "video4linux2", "-s", "1920x1080", "-i", "/dev/video0", "-ss", "0:0", "-frames", "1", f"./led-{lednum}.bmp"], check=True)

print (":)")

