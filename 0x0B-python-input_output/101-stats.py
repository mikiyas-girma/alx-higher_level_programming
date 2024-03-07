#!/usr/bin/python3
"""this module contains functions to parse stdin and print statistics"""

import sys
from collections import defaultdict


def parse_log_line(line):
    """parse the line in to file_size and status_code"""
    parts = line.split()
    file_size = int(parts[-1])
    status_code = int(parts[-2])
    return file_size, status_code


def print_statistics(total_size, status_counts):
    """print accumulated metrics"""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.key()):
        print("{}: {}".format(status_code, status_counts[status_code]))


def main():
    """main function """
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            file_size, status_code = parse_log_line(line)
            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1

        if line_count % 10 == 0:
            print_statistics(total_size, status_counts)
            print()

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

    if __name__ == "__main__":
        main()
