# Cleaning up sections of the camp - each section has a unique ID and each elve has a range
# Noticed many of the section assignments overlap
# Sections are assigned in comma seprated lines as ranges
# We are looking for fully contained overlap (6-6, 4-6)

def main():
    # pure overlap
    naughty_pairs = []
    # partial overlap
    extra_naughty_pairs = []
    with open("cleaning_pairs.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            clean_line = line.strip()
            elf_1_assign, elf_2_assign = clean_line.split(",")
            e1 = [int(i) for i in elf_1_assign.split("-")]
            e2 = [int(i) for i in elf_2_assign.split("-")]

            if (e1[0] >= e2[0] and e1[1] <= e2[1]) or (e1[0] <= e2[0] and e1[1] >= e2[1]):
                naughty_pairs.append([e1, e2])

            # part 2: which have any amount of partial overlap

            if (e1[0] <= e2[0] and e1[1] >= e2[0]) or (e2[0] <= e1[0] and e2[1] >= e1[0]):
                extra_naughty_pairs.append([e1, e2])

    print("Total overlap:")
    print(len(naughty_pairs))

    print(extra_naughty_pairs)
    print(len(extra_naughty_pairs))

if __name__ == "__main__":
    main()
