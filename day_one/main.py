import re

def main():
    elves = []
    counter = 0
    with open("elf_calories.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line.strip():
                counter += int(line)
            else:
                elves.append(counter)
                counter = 0

    print("Highest calories amount:")
    print(max(elves))

    print("Top three calorie amounts combined:")
    elves.sort()
    print(sum(elves[-3:]))
            


if __name__ == "__main__":
    main()
