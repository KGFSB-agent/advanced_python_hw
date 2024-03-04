import sys
import os

def wc(file_paths):
    total_lines = 0
    total_words = 0
    total_bytes = 0
    
    for file_path in file_paths:
        lines = 0
        words = 0
        bytes_count = 0
        file_name = os.path.basename(file_path)

        with open(file_path, 'r') as file:
            for line in file:
                lines += 1
                words += len(line.split())
                bytes_count += len(line.encode('utf-8'))

        total_lines += lines
        total_words += words
        total_bytes += bytes_count

        print(f"{lines}\t{words}\t{bytes_count}\t{file_name}")

    if len(file_paths) > 1:
        print(f"{total_lines}\t{total_words}\t{total_bytes}\ttotal")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        wc(sys.argv[1:])
    else:
        lines = 0
        words = 0
        bytes_count = 0

        for line in sys.stdin:
            lines += 1
            words += len(line.split())
            bytes_count += len(line.encode('utf-8'))

        print(f"{lines}\t{words}\t{bytes_count}")