import sys

def main(lines):
    num_of_gardens = int(lines[0])
    level_of_blue = list(map(int, lines[1].split()))

    for i in range(num_of_gardens):
        copied_level_of_blue = level_of_blue.copy()
        copied_level_of_blue.remove(copied_level_of_blue[i])
        print(max(copied_level_of_blue))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
