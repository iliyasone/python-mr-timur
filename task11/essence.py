from math import ceil


def get_information_weight(n: int) -> int:
    for i in range(1, n):
        if 2 ** i >= n:
            return i

assert get_information_weight(15) == 4
assert get_information_weight(16) == 4
assert get_information_weight(7) == 3


for n in range(2, 100):
    i = get_information_weight(n)
    serial_number = i * 229
    serial_number_byte = ceil(i * 229 / 8) 
    if serial_number_byte * 703_569 <= 77 * 1024 * 1024:
        print(n)