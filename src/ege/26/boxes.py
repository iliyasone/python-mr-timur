content = """213 610
412 1132
626 1337
80 746
653 818
155 968
843 1182
453 889
107 1296
120 1275
591 968
607 1299"""

passangers = []
for line in content.split('\n'):
    start, finish = map(int, line.split())
    passangers.append((start, finish))

def take_second(pair):
    return pair[1]

take_second = lambda pair: pair[1]

passangers.sort(key=lambda pair: pair[0])
print(passangers)