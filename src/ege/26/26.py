delta_visitors = [0] * 60 * 24 # 1440

with open('files/26/27.06.23.txt') as file:
    n = int(file.readline())

    for line in file.readlines():
        enter, exit = map(int, line.split())
        delta_visitors[enter] += 1
        delta_visitors[exit] -= 1    
# 0 2
# 2 3

current_visitors = 0
max_visitors = 0
for t in range(60*24):
    current_visitors += delta_visitors[t]

    if current_visitors > max_visitors:
        max_visitors = current_visitors
    

print(max_visitors)

# [10, 0, 0, 0, 0, -10+11]
