def check(list1, val):
    return(all(x < val for x in list1))

def number_of_trees_until_blocked(list1, val):
    counter = 0
    for tree in list1:
        counter += 1

        if tree >= val: 
            break

    return counter

def main():
    rows = []
    scenic_scores = []
    with open("forrest.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            rows.append([int(c) for c in line])

    visible_trees = []
    for ri, row in enumerate(rows):
        for ti, tree in enumerate(row):
            left = row[:ti]
            right = row[(ti + 1):]
            column = [c[ti] for c in rows]
            above = column[:ri]
            below = column[(ri + 1):]

            if not right or not left or not above or not below:
                visible_trees.append(tree)
            elif check(left, tree) or check(right, tree) or check(above, tree) or check(below, tree):
                visible_trees.append(tree)
                left.reverse()
                above.reverse()
                lu = number_of_trees_until_blocked(left, tree)
                ru = number_of_trees_until_blocked(right, tree)
                au = number_of_trees_until_blocked(above, tree)
                bu = number_of_trees_until_blocked(below, tree)
                if (lu * ru * au * bu) == 319275:
                    print(f'tree: {tree}')
                    print(f'left: {left}')
                    print(f'right: {right}')
                    print(f'above: {above}')
                    print(f'below: {below}')
                    print(f'row: {row}')
                    print(f'column: {column}')
                    print(f'lu: {lu}')
                    print(f'ru: {ru}')
                    print(f'au: {au}')
                    print(f'bu: {bu}')

                scenic_scores.append(lu * ru * au * bu)

    print(len(visible_trees))
    print(max(scenic_scores))
if __name__ == "__main__":
    main()
