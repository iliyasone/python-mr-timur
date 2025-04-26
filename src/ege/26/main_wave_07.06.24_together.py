with open("files/26/26_17537.txt") as file:
    n, m, k = map(int, file.readline().split())
    # m - рядок, k - количество мест в ряду
    max_row_by_column = [m - 1] * k
    """максимальное место куда можно сесть 
    по рядам
    """

    for line in file.readlines():
        row_occ, column_occ = map(int, line.split())
        row_occ -= 1
        column_occ -= 1
        if row_occ <= max_row_by_column[column_occ]:
            max_row_by_column[column_occ] = row_occ - 1

max_row = 0
for i in range(k - 1, 0, -1):
    candidate_row = min(max_row_by_column[i], max_row_by_column[i - 1])
    if candidate_row > max_row:
        max_row = candidate_row
        answer_column = i

print(max_row + 1, answer_column + 1)
