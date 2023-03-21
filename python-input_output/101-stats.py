import sys

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin):
        ip_address, _, _, _, _, status_code, file_size = line.split()
        total_file_size += int(file_size)
        status_code_counts[int(status_code)] += 1

        if (i + 1) % 10 == 0:
            print("Total file size: File size: {}".format(total_file_size))
            for status_code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print("{}: {}".format(status_code, count))

except KeyboardInterrupt:
    print("Total file size: File size: {}".format(total_file_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(status_code, count)))
