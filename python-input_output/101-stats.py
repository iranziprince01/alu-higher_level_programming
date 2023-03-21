#!/usr/bin/python3
# Script that reads stdin line by line and computes metrics


import sys

status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
metrics = {"total_size": 0, "status_code_count": {code: 0 for code in status_codes}}

try:
    for i, line in enumerate(sys.stdin):
        if i % 10 == 0 and i > 0:
            print("Total file size: File size: {}".format(metrics["total_size"]))
            for code in sorted(metrics["status_code_count"].keys()):
                if metrics["status_code_count"][code] > 0:
                    print("{}: {}".format(code, metrics["status_code_count"][code]))
        parts = line.split()
        code = parts[3]
        size = int(parts[4])
        metrics["total_size"] += size
        if code in metrics["status_code_count"]:
            metrics["status_code_count"][code] += 1
except KeyboardInterrupt:
    print("Total file size: File size: {}".format(metrics["total_size"]))
    for code in sorted(metrics["status_code_count"].keys()):
        if metrics["status_code_count"][code] > 0:
            print("{}: {}".format(code, metrics["status_code_count"][code]))


"""
This module reads input from stdin in the following format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

For every 10 lines of input or when a keyboard interruption (CTRL + C) is detected, the module prints the following statistics since the beginning:
- Total file size: File size: <total size> (sum of all previous file sizes)
- Number of lines by status code (in ascending order):
    <status code>: <number>

Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.

Note: This module assumes that the input format is consistent with the format specified in the prompt and does not handle any errors that may arise from malformed input.
"""

