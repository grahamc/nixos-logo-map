#!/usr/bin/env nix-shell
#!nix-shell -i bash -p python3 python3.pkgs.pillow

seq 0 359 | xargs -n1 -P $(nproc) python3 ./brightest.py