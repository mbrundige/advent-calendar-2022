# Part One
# one elf manages loading of rucksacks
# rucksack has two large compartments
# all items of given type are meant for one rucksack- meaning there can't be dups between two departments
# all item types have a single upper or lower case id (A is different than a)
# single line = rucksack
# half of that line = compartment

# Part Two
# elves are divided in groups of three
# each elve carries a badge and is the only item type by all three

def main():
    like_item_vals = []
    all_items = []
    with open("rucksack_data.txt") as f:
        like_item_vals = []
        while True:
            line = f.readline()
            if not line:
                break

            line = line.strip()
            all_items.append(line)
            split = int((len(line) - 1) / 2) + 1
            comp_one = line[:split]
            comp_two = line[split:]

            rucksack_like_items = []

            for l in comp_one:
                if l in comp_two and not l in rucksack_like_items:
                    like_item_vals.append(calc_character_value(l))
                    rucksack_like_items.append(l)

    print("Sum of errors:")
    print(sum(like_item_vals))

    # Finding the badge
    badge_item_vals = []
    three_elve_groups = list(zip(*[iter(all_items)]*3))
    for group in three_elve_groups:
        grp_rucksack_like_items = []
        for l in group[0]:
            if l in group[1] and l in group[2] and l not in grp_rucksack_like_items:
                badge_item_vals.append(calc_character_value(l))
                grp_rucksack_like_items.append(l)

    print("Sum of badge priorities:")
    print(sum(badge_item_vals))

def calc_character_value(char):
    value = 0
    if char.isupper():
        value = (ord(char) - 65) + 27
    else:
        value = ord(char) - 96
    return value


if __name__ == "__main__":
    main()
