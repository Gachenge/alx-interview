#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys
"""show total file size, each status code and how many times it is incurred"""

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
line = 0

try:
    for inputs in sys.stdin:
        lists = inputs.split(" ")
        if len(lists) > 4:
            code = lists[-2]
            size = int(lists[-1])
            total_size += size
            if code in status_codes.keys():
                status_codes[code] += 1
            line += 1
        if line == 10:
            line = 0
            print(f"File size: {total_size}")
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print(f"{key}: {value}")
except Exception as e:
    pass

finally:
    if code in status_codes:
        for key, value in sorted(status_codes.items()):
            if key == code:
                value += 1
    print(f"File size: {total_size}")
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print(f"{key}: {value}")
