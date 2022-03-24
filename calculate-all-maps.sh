#!/bin/sh

for i in $(seq 1 255); do
    color=$(printf '%02x%02x%02x' $i $i $i);

    if [ ! -f "combined-$color.json" ]; then
        ./calculate-map.sh "$color";
    fi
done