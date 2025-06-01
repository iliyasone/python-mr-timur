def moves(s: int):
    candidates = [s - 1, s - 2, s - 4]
    return [move for move in candidates if move >= 0]


def is_position_winning(s: int) -> bool:
    """    
    Возвращает `True` если позиция выигрышная
    Возвращает `False` если позиция проигршныя
    """
    if s == 0:
        return False
    for h in moves(s):
        if is_position_winning(h) is False:
            return True
    return False


def is_position_winning_in_turns(s: int, turns: int) -> bool | None: 
    """Вариант реализиции который высчитывает ходы:
    Если позиция не разрешается в `turns` ходов то возвращает `None`
    """
    ...


def is_position_winning_count_turns(s: int) -> tuple[bool, int]:
    """
    Альтернативная идея: 
    возвращать количество ходов сразу, за сколько позиция 
    точно реализуется
    """
    return (True, 3)


# пример простой рекурсии
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
