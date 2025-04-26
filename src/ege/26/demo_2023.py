boxes = [100, 97, 94, 91, 88, 85, 80, 76, 70]
answer = [boxes[0]]
for box in boxes[1:]:
    if answer[-1] - box >= 3:
        answer.append(box)
print(answer)
print(len(answer), answer[-1])
