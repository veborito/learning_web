file = open("inputs/input_3")
lines = [line.strip() for line in file]
matrice = [[el for el in line] for line in lines]
lenM = len(matrice)
numbers = []
for i in range(lenM):
    hits = 0
    number = ""
    info = []
    start = 0
    end = 0
    j = 0
    while j < lenM:
        while j < lenM and matrice[i][j].isnumeric():
            #check les alentours
            number += matrice[i][j]
            if i + 1 < lenM and not matrice[i + 1][j].isnumeric() and matrice[i + 1][j] != '.':
                hits = 1
                info = (i + 1, j)
            if i - 1 >= 0 and not matrice[i - 1][j].isnumeric() and matrice[i - 1][j] != '.':
                hits = 1
                info = (i - 1, j)
            if i + 1 < lenM and j + 1 < lenM and not matrice[i + 1][j + 1].isnumeric() and matrice[i + 1][j + 1] != '.': # distribution normalement
                hits = 1
                info = (i + 1, j + 1)
            if i + 1 < lenM and j - 1 >= 0 and not matrice[i + 1][j - 1].isnumeric() and matrice[i + 1][j - 1] != '.':
                hits = 1
                info = (i + 1, j - 1)
            if i - 1 >= 0 and j - 1 >= 0 and not matrice[i - 1][j - 1].isnumeric() and matrice[i - 1][j - 1] != '.':
                hits = 1
                info = (i - 1,j - 1)
            if i - 1 >= 0 and j + 1 < lenM and not matrice[i - 1][j + 1].isnumeric() and matrice[i - 1][j + 1] != '.':
                hits = 1
                info = (i - 1, j + 1)
            if j + 1 < lenM and not matrice[i][j + 1].isnumeric() and matrice[i][j + 1] != '.':
                hits = 1
                info = (i, j + 1)
            if j - 1 >= 0 and not matrice[i][j - 1].isnumeric() and matrice[i][j - 1] != '.':
                hits = 1
                info = (i, j - 1)
            j += 1
        if hits:
            numbers.append([int(number), info])
            hits = 0
        else:
            j += 1
        number = ""
        info = []
gears = []
gear = 1
print(numbers)
for i in range(len(numbers)):
    is_gear = 0
    for j in range(i + 1, len(numbers)):
        if numbers[i][1] == numbers[j][1]:
            is_gear = 1
            gear *= numbers[j][0]
    if is_gear:
        gear *= numbers[i][0]
        gears.append(gear)
        gear = 1

print(sum(gears))
