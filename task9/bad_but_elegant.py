### vvv
with open('example.csv') as file:
    for line in file:
        ...
### ---
for line in open('example.csv'):
    ...
# ! файл может не закрыться но нам пофиг
### ^^^

'Привет\n\n'.strip()
# strip удаляет '\n'