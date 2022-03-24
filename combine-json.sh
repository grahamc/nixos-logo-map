#!/bin/sh

(
    first=1
    echo "["
    for f in $(find . -name 'led-*.json'); do
        if [ $first -eq 0 ]; then
            echo ","
        else
            first=0
        fi
        cat "$f"
    done
    echo "]"
) > combined.json
