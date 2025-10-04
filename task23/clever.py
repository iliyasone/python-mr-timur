def path_finder(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    return path_finder(start + 1, end) \
         + path_finder(start * 2, end) \
         + path_finder(start * 3, end)


paths_30 = path_finder(10, 30) * path_finder(30, 70)
# 10 -> 30 -> 60 -> 70
# 10 -> 30 ->x[60]-> 70

paths_60 = path_finder(10, 60) * path_finder(60, 70)
# 10 -> 30 -> 60 -> 70
# 10 ->x[30]-> 60 -> 70

paths_30_AND_60 = path_finder(10, 30) * path_finder(30, 60) * path_finder(60, 70)

print(paths_30 + paths_60 - paths_30_AND_60)

# 10 -> 30 -> 60 -> 70
# 10 -> 30 -> 60 -> 70
# 10 ->x[30]-> 60 -> 70
# 10 -> 30 ->x[60]-> 70
