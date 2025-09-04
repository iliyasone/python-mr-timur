# https://kompege.ru/task?id=23753
import string
digits = string.digits + string.ascii_lowercase
digits_base_29 = digits[:29]

for x in digits_base_29:
    base_29 = str(x)
    print(f'{base_29=}\t= {int(base_29, 29)}')
    ...