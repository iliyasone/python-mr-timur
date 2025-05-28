def moves(s: int):
    candidates = [s - 1, s - 2, s - 4]
    return [move for move in candidates if move >= 0]


def is_position_winning(s: int) -> tuple[bool, int]:
    if s == 0:
        return False, 0
    for h in moves(s):
        
        if is_position_winning(h) is False:
            return True
    return False


is_position_winning(3)