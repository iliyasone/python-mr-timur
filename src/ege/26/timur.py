f = open('files/26/26_17537.txt') #9990 99938 6660
n, m, k = map(int, f.readline().split())
a = f.readlines()
f.close()

max_condidates = list()
condidates = [m+1] * k
for i in range(k):
    condidates_ryad = list()
    for i3 in a:
        ryad = int(i3.split()[0])
        stolbec = int(i3.split()[1]) - 1
        if i == stolbec:
            condidates_ryad.append(ryad)
    if len(condidates_ryad) > 0:
        condidates[i] = min(condidates_ryad)

print('condidates done')
max_row = 0
max_i = 0
for i in range(k -1, 0, -1):
    candidate_max_row = min(condidates[i], condidates[i-1])
    if candidate_max_row > condidates[i]:
        max_row = candidate_max_row
        max_i = i

print(max_row-1, max_i+1)