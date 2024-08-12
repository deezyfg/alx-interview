#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

from collections import defaultdict
import sys


def print_stats(total_size, status_codes):
    """Print accumulated metrics.

    Args:
        total_size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(total_size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":

    # Initialize variables
    total_size = 0
    status_codes = defaultdict(int)
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            # Print stats every 10 lines
            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 1
            else:
                line_count += 1

            # Split the line into components
            line = line.split()

            # Update total file size
            try:
                total_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            # Update status code counts
            try:
                if line[-2] in valid_codes:
                    status_codes[line[-2]] += 1
            except IndexError:
                pass

        # Print final stats after reading all lines
        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Print stats on keyboard interrupt
        print_stats(total_size, status_codes)
        raise
