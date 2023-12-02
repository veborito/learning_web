with open("inputs/input_1") as file:
    all_numbers = []
    for line in file:
        numbers = []
        for i in range(len(line)):
            if line[i : i + 3] == 'one':
                numbers.append('1')
            elif line[i : i + 3] == 'two':
                numbers.append('2')
            elif line[i : i + 5] == 'three':
                numbers.append('3')
            elif line[i : i + 4] == 'four':
                numbers.append('4')
            elif line[i : i + 4] == 'five':
                numbers.append('5')
            elif line[i : i + 3] == 'six':
                numbers.append('6')
            elif line[i : i + 5] == 'seven':
                numbers.append('7')
            elif line[i : i + 5] == 'eight':
                numbers.append('8')
            elif line[i : i + 4] == 'nine':  
                numbers.append('9')
            elif line[i].isnumeric():
                numbers.append(line[i])
        all_numbers.append(numbers)
    somme = []
    for numbers in all_numbers:
        if len(numbers) == 1:
            somme.append(int(numbers[0] + numbers[0]))
        else:
            somme.append(int(numbers[0] + numbers [-1]))
print(sum(somme))

