def main():
    lst = 'АБЗИ'
    counter = 0
    for a in range(0, 4):
        for b in range(0, 4):
            for c in range(0, 4):
                for d in range(0, 4):
                    counter += 1
                    word = lst[a] + lst[b] + lst[c] + lst[d]
                    # print(counter, word)
                    if word == 'ИЗБА':
                        print(counter, word)
                        return
main()