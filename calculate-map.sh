#!/bin/sh

set -eux

color=$1

./logo-capture-frames.py "$color"
./calculate-all-brightness.sh
./combine-json.sh

rm ./led-*.bmp
rm ./led-*.json
mv combined.json "combined-$color.json"