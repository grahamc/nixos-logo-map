#!/usr/bin/env nix-shell
#!nix-shell -i bash -p imagemagick

./plot-all-png.sh

echo "Producing plots.gif"

convert -delay 30 -loop 0 $(
    for i in $(seq 1 255); do
        file=$(printf 'plot-%02x%02x%02x.png' $i $i $i);
        if [ -f "$file" ]; then
            echo $file
        fi
    done
) plots.gif
