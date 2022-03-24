#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p python3 ffmpeg

from pprint import pprint
import subprocess
import json

with open("./combined.json") as f:
    data = json.loads(f.read())

minY = None
maxY = None

for led in data:
    if minY is None:
        minY = led['y']
    if maxY is None:
        maxY = led['y']
    
    if led['y'] > maxY:
        maxY = led['y']
    if led['y'] < minY:
        minY = led['y']

centerY = maxY - ((maxY - minY) / 2)
print(f"Max: {maxY}")
print(f"Min: {minY}")
print(f"Center: {centerY}")

bottomColor = '0000ff'
middleColor = '000000'
topColor = 'ffaa00'
buffer = 50

allLeds = []
top = []
middle = []
bottom = []

for led in data:
    allLeds.append(int(led['led']))
    if led['y'] > (centerY + buffer):
        top.append(int(led['led']))
    elif led['y'] > (centerY - buffer):
        middle.append(int(led['led']))
    else:
        bottom.append(int(led['led']))

print(f"Count top: {len(top)}")
print(f"Count middle: {len(middle)}")
print(f"Count bottom: {len(bottom)}")

allLeds = sorted(allLeds)
top = sorted(top)
middle = sorted(middle)
bottom = sorted(bottom)

colors = []
for led in allLeds:
    if led in top:
        colors.append(topColor)
    elif led in middle:
        colors.append(middleColor)
    elif led in bottom:
        colors.append(bottomColor)

subprocess.run(["curl", "-v", "http://10.5.4.51:3030?message=" + (",".join(colors))], check=True)
subprocess.run(["ffmpeg", "-f", "video4linux2", "-s", "1920x1080", "-i", "/dev/video0", "-ss", "0:0", "-frames", "1", "./rendered.png"], check=True)
