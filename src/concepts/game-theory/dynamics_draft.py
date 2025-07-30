def moves(h: int):
    return h + 3, h * 3, h + h**2


WIN_LIMIT = 666

is_position_winning = [None] * WIN_LIMIT
in_turns = [0] * WIN_LIMIT


# выигрыш в 1 ход
for s in range(WIN_LIMIT):
    if any(h >= WIN_LIMIT for h in moves(s)):
        is_position_winning[s] = True
        in_turns[s] = 1


# выигрыш на 2 ход (1 ход вани)
for s in range(WIN_LIMIT):
    if all(h < WIN_LIMIT and is_position_winning[h] is True for h in moves(s)):
        is_position_winning[s] = False
        in_turns[s] = 2


# выигрыш на 3 ход
for s in range(WIN_LIMIT):
    if any(h < WIN_LIMIT and is_position_winning[h] is False for h in moves(s)):
        is_position_winning[s] = True
        in_turns[s] = 3

# выигрыш на 4 ход (2 ход вани)
for s in range(WIN_LIMIT):
    if all(h < WIN_LIMIT and is_position_winning[h] is True for h in moves(s)):
        is_position_winning[s] = False
        in_turns[s] = 4


# выигрыш вани не гаранитровано
for s in range(WIN_LIMIT):
    if any(h < WIN_LIMIT and is_position_winning[h] is True for h in moves(s)):
        print(s)


# вывод в файл
with open("table.txt", "w") as file:
    for s in range(WIN_LIMIT):
        file.write(f"{s}\t{is_position_winning[s]}\t{in_turns[s]}\n")
