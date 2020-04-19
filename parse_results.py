#!/usr/bin/env python3

import re
from sys import argv, stderr

NOT_DETECTED_INDEX = 2
TP_TN_INDEX = 32
FP_FN_INDEX = 33
STAT_REGEX = re.compile(r'(?:True|False) (?:positives|negatives):\s+(\d+)')
HEADER = ['combo', 'tp', 'fn', 'tn', 'fp']


def main():
    file = argv[1]
    malware_id = argv[2]
    with open(file, 'r') as f:
        lines = f.readlines()

    if lines[NOT_DETECTED_INDEX] != '\n':
        lines.pop(NOT_DETECTED_INDEX)

    tp_tn_line = lines[TP_TN_INDEX]
    fp_fn_line = lines[FP_FN_INDEX]
    try:
        tp, tn = STAT_REGEX.findall(tp_tn_line)
        fp, fn = STAT_REGEX.findall(fp_fn_line)
        print(','.join(HEADER))
        print(','.join([malware_id, tp, fn, tn, fp]))
    except ValueError:
        print(f'Failed to unpack stats from regex for ID {malware_id}', file=stderr)


if __name__ == '__main__':
    main()

