k = 0
for line in open("9_23268.csv"):
    k += 1
    ### vvv
    numbers = [int(x) for x in line.split(",")]
    ### ---
    numbers = list(map(int, line.split(",")))
    ### ^^^

    ### vvv
    repeat_2 = [x for x in numbers if numbers.count(x) == 2]
    ### ---
    repeat_2 = []
    for x in numbers:
        if numbers.count(x) == 2:
            repeat_2.append(x)
    ### ^^^

    repeat_1 = []
    for x in numbers:
        if numbers.count(x) == 1:
            repeat_1.append(x)

    if len(repeat_2) == 4 and len(repeat_1) == 3:
        avg_repeated = sum(repeat_2) / len(repeat_2)
        max_unique = max(repeat_1)
        if avg_repeated < max_unique:
            print(k)
            break