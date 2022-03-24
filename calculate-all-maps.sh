#!/bin/sh

for i in $(seq 1 255); do
    color=$(printf '%02x%02x%02x' $i $i $i);
    ./calculate-map.sh "$color";
done