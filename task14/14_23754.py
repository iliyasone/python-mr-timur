def perevod(n: int, base: int) -> str:
    b = ''
    while n >= base:
        b += str(n % base)
        n = n // base
    b = ''.join(reversed(b + str(n)))
    return b


# test for all numbers x = [0..19]
for x in range(20):
    base_11_number = perevod(x, 11)
    print(f'base 10: {x} \tbase 11 {base_11_number}')
    assert int(base_11_number, 11) == x, x