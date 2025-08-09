from itertools import product

n = 1
for word in product(sorted("ТЕОРИЯ"), repeat=6):
    # print(n, *word)
    # проверить что всё работает
    if n % 2 == 1 and word[0] not in "РТЯ" and word.count("И") >= 2:
        print(n, *word)
    n += 1