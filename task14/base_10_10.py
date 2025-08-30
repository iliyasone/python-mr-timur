# number = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
number = 2727
def to_base(q: int, base: int) -> list[int]:
    result: list[int] = []
    while q > 0:
        result.append(q % base)
        print(q % base)
        q = q // base

    result.reverse()
    return result

count = 0
for digit in to_base(number, 27):
    if digit > 9:
        count += 1
print(count)