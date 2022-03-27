#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p python3 ffmpeg

from pprint import pprint
import subprocess
import json
from math import floor, ceil

def intersperse(elem, list):
    result = []
    for e in list:
      result.extend([e, elem])
    return result[:-1]

with open("./combined-0f0f0f-manipulated.json") as f:
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

height = maxY - minY
centerY = maxY - (height / 2)

bufferStripes = False
stripes = [
    '4da6ff', # blue
    '4da6ff', # blue

    'ff2020', # pink
    'ff2020', # pink

    'ffffff', # white
    'ffffff', # white
    #'ffffff', # white

    'ff2020', # pink
    'ff2020', # pink
    
    '4da6ff', # blue
    '4da6ff', # blue
]

# bufferStripes = True
# stripes = [
#     '0000ff',
#     'ffaa00'
# ]

if bufferStripes:
    stripes = intersperse('000000', stripes)

stripeHeight = ceil(height / len(stripes))


print(f"Max: {maxY}")
print(f"Min: {minY}")
print(f"Stripes: {len(stripes)}")
print(f"Stripe height: {stripeHeight}")

colors = list(range(0, 360))

for led in data:
    stripeNum = floor((led['y'] - minY)/ (stripeHeight))
    color = stripes[min(stripeNum, len(stripes) - 1)]
    colors[int(led['led'])] = color

subprocess.run(["curl", "-v", "http://10.5.4.51:3030?message=" + (",".join(colors))], check=True)
while True:
    try:
        subprocess.run(["ffmpeg", "-y", "-f", "video4linux2", "-s", "1920x1080", "-i", "/dev/video0", "-ss", "0:0", "-frames", "1", f"./snap.png"], check=True)
        break
    except subprocess.CalledProcessError:
        pass
