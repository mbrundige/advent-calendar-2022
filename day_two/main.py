def main():
    # Rock, Paper, Scissors
    decison_map = [
        ("A", [2, 0, 1]),
        ("B", [0, 1, 2]),
        ("C", [1, 2, 0])
    ]

    running_score = 0
    with open("rps_data.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            opp_selection, outcome_ct = line.split(" ")

            outcome = 0
            if outcome_ct == "Y":
                outcome = 1
            elif outcome_ct == "Z":
                outcome = 2

            mapping = [i for i in decison_map if i[0] == opp_selection][0]
            running_score += (outcome * 3) + (mapping[1][outcome] + 1)
            
    print("My score:")
    print(running_score)


if __name__ == "__main__":
    main()
