#!/usr/bin/env python3

import argparse


FIELDS_LINE_INDEX = 6
TYPES_LINE_INDEX = 7
FIRST_RECORD_INDEX = 8
IS_MAL_FIELD = '\tis_malicious'
IS_MAL_TYPE = '\tstring'
MS_UPDATE_TOKENS = ['msdownload', 'Microsoft-CryptoAPI', 'windowsupdate.com']


def main(args):
    is_benign = args.benign
    file_name = args.file
    ext_index = file_name.index('.decanter')
    output_file_name = file_name[:ext_index] + '.label' + file_name[ext_index:]
    print(f'Labelling {file_name} and saving to {output_file_name}')
    with open(file_name, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    lines[FIELDS_LINE_INDEX] += IS_MAL_FIELD
    lines[TYPES_LINE_INDEX] += IS_MAL_TYPE

    for i in range(FIRST_RECORD_INDEX, len(lines) - 1):
        if is_benign:
            lines[i] += '\t0'
        elif any(token in lines[i] for token in MS_UPDATE_TOKENS):
            lines[i] += '\t0'
        else:
            lines[i] += '\t1'

    with open(output_file_name, 'w') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Label outgoing HTTP requests from Bro/Zeek logs.")
    parser.add_argument('-f', '--file', type=str, help='Log file to operate on.')
    parser.add_argument('-b', '--benign', action='store_true',
                        help='Flag to indicate that the entire log file contains benign requests.')
    args = parser.parse_args()
    if args.file:
        main(args)
    else:
        parser.print_help()

