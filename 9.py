NUMBERS = 6
result = 0
with open('9.txt') as f:
    for line in f:
        numbers = list(map(int, line.split('\t')))
        occurrences = [0] * NUMBERS
        repeated_numbers = []
        unique_numbers = []
        for i in range(NUMBERS):
            occurrence = numbers.count(numbers[i])
            occurrences[i] = occurrence
            if occurrence == 1:
                unique_numbers.append(numbers[i])
            else:
                repeated_numbers.append(numbers[i])
        occurrences.sort()
        if occurrences != [1, 1, 1, 3, 3, 3]:
            continue
        if sum(repeated_numbers)**2 > sum(unique_numbers)**2:
            result += 1
print(result)