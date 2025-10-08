is_first_5_digit = open("17_23376.txt", "r")
lines = list(map(int, is_first_5_digit.readlines()))
five_digit_37 = list()
pairs = list()
sum_of_pairs = list()
for n in lines:
    if len(str(abs(n))) == 5 and str(n)[-2:] == "37":
        five_digit_37.append(n)
max_five_digit_37 = max(five_digit_37)
for n in range(len(lines) - 1):
    is_first_5_digit = len(str(abs(lines[n]))) == 5
    # Первое число пятизначное
    is_second_5_digit = len(str(abs(lines[n + 1]))) == 5
    # Второе число пятизначное
    a = is_first_5_digit and not is_second_5_digit
    b = is_second_5_digit and not is_first_5_digit
    c = ((lines[n] + lines[n + 1]) ** 2) > max_five_digit_37**2
    # Сумма в квадрате > max_five_digit_37 в квадрате
    if (a or b) and c:
        pairs.append((lines[n], lines[n+1]))
        sum_of_pairs.append(lines[n] + lines[n + 1])
print(pairs)
print(max(sum_of_pairs), len(sum_of_pairs))

# ДЗ: ЕГЭ досрок 2025
# https://kompege.ru/task?id=21416
#

