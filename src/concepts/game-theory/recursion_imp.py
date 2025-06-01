def moves(s: int):
    candidates = [s - 1, s - 2, s - 4]
    return [move for move in candidates if move >= 0]


def is_position_winning(s: int, turns: int) -> bool | None:
    if s == 0:
        return False
    if turns == 0:
        return None
    if all(is_position_winning(move, turns-1) == True for move in moves(s)):
        return False
    if any(is_position_winning(move, turns-1) == False for move in moves(s)):
        return True
    return None


# Критерии Успешной Рекурсии
# - Крайний случай (ты знаешь без ответ без необходимости рекурсивного вызова)
# - Шаг рекурсии приближает тебя к крайнему случаю


# Петя1 Ваня1 Петя2


# Петя выигрывает своим вторым ходом
# Независимо от игры Вани
for s in range(1, 15+1):
    if is_position_winning(s, 3) is not None:
        continue
    if is_position_winning(s, 5) is True:
        print(s)


"""
Задание 20.

Найдите два наименьших значения S, при которых 
у Пети есть выигрышная стратегия, позволяющая ему выиграть вторым или третьим ходом в зависимости от хода Вани, 

при этом у него нет стратегии, которая позволит ему гарантированно выиграть своим вторым ходом.

"""