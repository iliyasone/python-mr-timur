def transform(b: int):
    a = bin(b)
    a = a[2:]

    c = 0

    for i in range(len(a)):
        c += int(a[i])

    a = a[2:]
    if c % 2 == 0:
        a = '10' + a + '0'
    else:
        a = '11' + a + '1'

    return int(a,2)


for i in range(2, 100):
    if transform(i) < 35:
        print(i)