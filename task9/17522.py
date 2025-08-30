list_a: list[list[str]] = list()
with open('9_17522.csv', 'r') as f:
    for s in f:
        list_a.append(s.split(';'))

count1 = 0

for list_b in list_a:
    a = (sum(map(int, list_b)) - max(map(int, list_b))) > max(map(int, list_b))
    b = list()
    for n in range(len(list_b)):
        b.append(list_b.count(list_b[n]))
    if b.count(2) == 2 and b.count(1) == 2:
        b = True
    if a == True and b == True:
        count1 += 1
print(count1)
