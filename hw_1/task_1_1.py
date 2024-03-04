import sys

def nl(file_path=None):
    if file_path:
        with open(file_path, 'r') as file:
            for num, line in enumerate(file, start=1):
                print(f"{num} {line}", end='')
    else:
        for num, line in enumerate(sys.stdin, start=1):
            print(f"{num} {line}", end='')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nl(sys.argv[1])
    else:
        nl()
