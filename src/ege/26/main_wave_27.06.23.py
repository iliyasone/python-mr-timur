with open("files/26/27.06.23.txt") as file:
    n = int(file.readline())

    delta = [0] * 24 * 60

    for _ in range(n):
        enter, exit = map(int, file.readline().split())

        delta[enter] += 1
        delta[exit] -= 1

    current_visititors = 0
    max_visitors = 0
    peaks = 0
    for i in range(24 * 60):
        current_visititors += delta[i]

        if current_visititors > max_visitors:
            max_visitors = current_visititors
            peaks = 1
        elif current_visititors == max_visitors and delta[i] > 0:
            peaks += 1
    print(peaks, max_visitors)
