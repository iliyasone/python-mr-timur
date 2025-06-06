"""19
№ 2365 (Уровень: Сложный)

Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может

а) забрать из кучи один камень;
б) забрать из кучи два камня;
в) забрать из кучи четыре камня.

Если камней в куче меньше, чем забирается, то такой ход выполнить нельзя. Игрок, забравший последний камень выигрывает. В начальный момент в куче было S камней, 1 ≤ S ≤ 15.

Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите максимальное значение S, когда такая ситуация возможна.

Задание 20.
Для условия игры из задания 19, ответьте на вопрос.

Найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия, позволяющая ему выиграть вторым или третьим ходом в зависимости от хода Вани, при этом у него нет стратегии, которая позволит ему гарантированно выиграть своим вторым ходом.


Задание 21.
Для условия игры из задания 19, ответьте на вопрос.

Найдите максимальное значение S, при котором Ваня имеет выигрышную стратегию, при которой он выигрывает при любой игре Пети.
"""


def moves(s: int):
    candidates = [s - 1, s - 2, s - 4]
    return [move for move in candidates if move >= 0]

def moves(s: int):
    """возвращает возможные позиции списком. """
    result = []
    if s - 1 >= 0:
        result.append(s - 1)
    if s - 2 >= 0:
        result.append(s - 2)
    if s - 4 >= 0:
        result.append(s - 4)
    return result


S_MAX = 15+1
is_position_winning = ['None'] * S_MAX
is_position_winning[0] = 'False'


# 1. Находим выигрышные позиции
for s in range(1, S_MAX):                        # смотрим все возможные позиции
    if 'None' in is_position_winning[s]:         # которые не заняты

        #  any(is_position_winning[move] is False for move in moves[s])
        if any(move == 0 for move in moves(s)):
            # есть хотя бы один ход который приводит к поражению противника
            is_position_winning[s] = 'True1'

# 2. Находим проигрышные позиции
for s in range(1, S_MAX):
    if 'None' in is_position_winning[s]:  
        if all('True' in is_position_winning[move] for move in moves(s)):
            is_position_winning[s] = 'False2'


for s in range(1, S_MAX):
    if 'None' in is_position_winning[s]:  
        if any('False' in is_position_winning[move] for move in moves(s)):
            is_position_winning[s] = 'True3'


# 2. Находим проигрышные позиции
for s in range(1, S_MAX):
    if 'None' in is_position_winning[s]:  
        if all('True' in is_position_winning[move] for move in moves(s)):
            is_position_winning[s] = 'False4'

for s in range(1, S_MAX):
    if 'None' in is_position_winning[s]:  
        if any('False' in is_position_winning[move] for move in moves(s)):
            is_position_winning[s] = 'True5'


# запись в файл
with open('table.txt', 'w') as file:
    for s in range(1, S_MAX):
        file.write(f'{s}\t{is_position_winning[s]}\n')
