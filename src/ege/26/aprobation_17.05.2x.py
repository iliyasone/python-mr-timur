# https://kompege.ru/task?id=8512
with open('files/26/26_8512.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    passengers = [[int(x) for x in line.split()] for line in file.readlines()]
    passengers.sort()
    print(passengers)
    cells = [0] * k

count = 0
for start, end in passengers:
    for i in range(k):
        if start > cells[i]:
            cells[i] = end
            count += 1
            break

print(count, i)