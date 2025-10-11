a = open('17_21416.txt', 'r')
lines = list(map(int, a.readlines()))
a.close()
sum_of_minus_n = 0
answers_list = list()
for i in range(len(lines)):
    if lines[i] < 0:
        sum_of_minus_n += lines[i]

for i in range(len(lines)-2):
    max_element = max([lines[i], lines[i+1], lines[i+2]])
    min_element = min([lines[i], lines[i+1], lines[i+2]])
    if max_element * min_element > sum_of_minus_n:
        answers_list.append(lines[i] + lines[i+1] + lines[i+2])
print(len(answers_list), abs(max(answers_list)))
