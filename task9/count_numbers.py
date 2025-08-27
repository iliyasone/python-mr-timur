line = [5, 25, 7, 25, 6, 5]

count_numbers = [0, 0, 0, 0, 0, 0]
for i in range(len(line)):
    count_numbers[i] = line.count(line[i])
# count_numbers == [2, 2, 1, 2, 1, 2]
count_3 = count_numbers.count(3) 
count_1 = count_numbers.count(1)
sum_without_max = sum(line) - max(line)