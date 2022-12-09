from collections import defaultdict

def main():
    sizes = defaultdict(int)
    path = []
    with open("linux_commands.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if line.startswith("$ cd"):
                d = line.split()[2]
                if d == "/":
                    path.append("/")
                elif d == "..":
                    last = path.pop()
                else:
                    path.append(f"{path[-1]}{'/' if path[-1] != '/' else ''}{d}")
            elif line[0].isnumeric():
                for p in path:
                    sizes[p] += int(line.split()[0])

    print(sum(s for s in sizes.values() if s <= 100_000))
    print(min(s for s in sizes.values() if s >= 30_000_000 - (70_000_000 - sizes['/'])))

if __name__ == "__main__":
    main()
