def main():
    sample = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
    
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    adjacent = lambda p1, p2: all([abs(p1[i] - p2[i]) <= 1 for i in range(2)])
    visited_1 = {(0, 0)}
    visited_9 = {(0, 0)}
    knots = [[0] * 2 for _ in range(10)]

    with open('movements.txt') as f:
        lines = f.read().splitlines()

    for l in lines:
        # get the direction for the head
        d = directions[l[0]]
        for _ in range(int(l[2:])): 
            for i in range(2): knots[0][i] += d[i]
            for k in range(9):
                h, t = knots[k:k+2]
                if not adjacent(h, t):
                    for i in range(2): t[i] += (h[i] != t[i]) * (2*(h[i] > t[i]) - 1)
            visited_1.add(tuple(knots[1]))
            visited_9.add(tuple(knots[9]))

    print(len(visited_1))
    print(len(visited_9))

if __name__ == "__main__":
    main()
