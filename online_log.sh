#!/usr/bin/env bash

source /home/zachary/Desktop/decanter/venv/bin/activate

python2 main.py --training $1 --testing $2 -o 0

deactivate

