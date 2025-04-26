# https://kompege.ru/task?id=2944
with open("files/26/26_2944.txt") as file:
    s, n = map(int, file.readline().split())
    disk = [int(x) for x in file.readlines()]
    disk.sort()

used_memory = 0
count_files = 0
for i in range(n):
    if used_memory + disk[i] <= s:
        used_memory += disk[i]
        count_files += 1
    else:
        used_memory -= disk[i-1]
        break

for i in range(n - 1, -1, -1):
    if used_memory + disk[i] <= s:
        used_memory += disk[i]
        break

print(count_files, disk[i])
