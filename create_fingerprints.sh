#!/usr/bin/env bash

# Benign log for training
BENIGN=$HOME/Documents/directed_studies/benign_traffic_vm.label.decanter
# Directory of malware logs for testing
MALWARE=$HOME/Documents/directed_studies/pcaps/logs_labelled

. venv/bin/activate

for log in $MALWARE/*
do
    malware_id=$(basename -s .label.decanter $log)
    python2 main.py --training $BENIGN --testing $log -o 1
    python2 main.py --csv ./ >> evaluation.txt
    python3 parse_results.py evaluation.txt $malware_id >> results.csv
    zip $malware_id evaluation.txt results.csv training_fingerprints.csv testing_fingerprints.csv
    rm evaluation.txt results.csv training_fingerprints.csv testing_fingerprints.csv
    mv "$malware_id.zip" zips/
done

