#!/usr/bin/env nix-shell
#!nix-shell -i bash -p python3 python3.pkgs.matplotlib

for i in $(seq 1 255); do
    color=$(printf '%02x%02x%02x' $i $i $i);
    if [ -f "combined-$color.json" ]; then
      if [ ! -f "combined-$color.svg" ]; then
        python3 ./plot-svg.py "$color";
      fi
    fi
done
