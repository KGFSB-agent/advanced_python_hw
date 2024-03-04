import sys
import os

def tail(file_path=None, num_lines=10):
    if file_path:
        file_name = os.path.basename(file_path)
        print(f"==> {file_name} <==")

        with open(file_path, 'r') as file:
            lines = file.readlines()
            last_lines = lines[-num_lines:]
            print(''.join(last_lines))
            print()
    else:
        lines = []
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            lines.append(line)
            if len(lines) > num_lines:
                del lines[0]

        last_lines = lines[-num_lines:]
        print(''.join(last_lines))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for file_path in sys.argv[1:]:
            tail(file_path)
    else:
        tail(num_lines=17)