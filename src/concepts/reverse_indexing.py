MAX_NUMBER = 10

data = [9, 1, 2, 1, 6, 7, 3, 2, 6, 1, 2, 1]

count = [0] * MAX_NUMBER
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^

for entry in data:
    count[entry] += 1

#   [0, 2, 1, 0, 0, 0, 0, 0, 0, 1]
#    ^  ^  ^  ^  ^  ^  ^  ^  ^  ^
# i: 0  1  2  3  4  5  6  7  8  9

for n in range(MAX_NUMBER):
    if count[n] > 0:
        print(f"{n}, " * count[n])
