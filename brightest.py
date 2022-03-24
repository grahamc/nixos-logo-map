#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p python3 python3.pkgs.pillow

from PIL import Image
import sys
import json

led = sys.argv[1]

image = Image.open(f"led-{led}.bmp")

maxBrightness = 0
bestX = 0
bestY = 0

width, height = image.size

for x in range(0, width):
    for y in range(0, height):
        brightness = sum(image.getpixel((x,y))) / 3
        if brightness > maxBrightness:
            maxBrightness = brightness
            bestX = x
            bestY = y
with open(f"led-{led}.json", "w") as f:
    f.truncate()
    f.write(json.dumps({
        "led": led,
        "x": bestX,
        "y": bestY,
        "brightness": maxBrightness 
    }))