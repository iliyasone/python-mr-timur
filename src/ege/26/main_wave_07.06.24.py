with open('files/26/26_17537.txt') as file: 
    n, m, k = map(int, file.readline().split())
    
    max_free_row: dict[int, int] = {}

    for line in file.readlines():
        row, col = map(int, line.split())

        
        max_free_row[col] = min(max_free_row.get(col, m), row - 1)

for i in range(1, m+1):
    print(i, max_free_row.get(i, 0),end=' ',sep='-')
print()

answer_row = 0
answer_col = 0

for col in range(k, 1, -1):  # идем с конца, от максимального номера мест
    r1 = max_free_row.get(col, m)
    r2 = max_free_row.get(col - 1, m)
    candidate_row = min(r1, r2)
    if candidate_row > answer_row:
        answer_row = candidate_row
        answer_col = col
print(answer_row, answer_col)
