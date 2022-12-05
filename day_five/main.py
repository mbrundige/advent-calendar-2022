import re
# supplies are stored in crates and they need rearranged
# ship has one giant cargo crane capable of moving the crates
# they don't know which crates will end up where

def main():
    # [[T, R, D, H, Q, N, P, B], [V, T, J, B, G, W]]
    # convert initial structure into 2D arrays
    columns = [[], [], [], [], [], [], [], [], []]
    with open("starting_ship.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            # fill in nil values
            line = line.replace("    ", " []")
            for i, c in enumerate([re.sub("\[|]", "", c) for c in line.split()]):
                if c != '':
                    columns[i].append(c)

    with open("movements.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip().replace(" ", "")
            only_numbers = re.sub("([a-z]+)", ",", line)[1:]
            qty, from_cargo, to_cargo = [int(i) for i in only_numbers.split(",")]

            idx_from = from_cargo - 1
            idx_to = to_cargo - 1
            items = columns[idx_from][:qty]
            for item in items:
                columns[idx_to].insert(0, item)
            columns[idx_from] = columns[idx_from][qty:]

    print(''.join([i[0] for i in columns]))

if __name__ == "__main__":
    main()
