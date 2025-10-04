# Исполнитель преобразует число на экране.
# У исполнителя есть три команды, которые обозначены латинскими буквами:
# A. Вычесть 1
# B. Вычесть 4
# C. Найти целую часть от деления на 3


def count_paths(start: int, end: int) -> int:
    if start < end:
        return 0
    if start == end:
        return 1
    if start == 7:
        return 0
    return (
        count_paths(start - 1, end)
        + count_paths(start - 4, end)
        + count_paths(start // 3, end)
    )


assert count_paths(6, 2) == 3

print(count_paths(19, 13) * count_paths(13, 2))
