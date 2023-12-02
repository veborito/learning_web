file = open("inputs/input_2")
lines = [line.strip() for line in file]
game_list = []
for line in lines:
    full_games = ", ".join(line.split(':')[1].split(';'))
    game_list.append([[game.strip(' ').split(' ')[1] , int(game.strip(' ').split(' ')[0])] for game in full_games.split(',')])

game_values = []
for game in game_list:
    values = {'blue': 0, 'red': 0, 'green': 0}
    for el in game:
        if el[0] == 'blue':
            if values['blue'] < el[1]:
                values['blue'] = el[1]
        if el[0] == 'green':
            if values['green'] < el[1]:
                values['green'] = el[1]
        if el[0] == 'red':
            if values['red'] < el[1]:
                values['red'] = el[1]
    game_values.append(values)

sol = 0

for game in game_values:
    mult = 1
    for v in game.values():
        mult *= v
    sol += mult

print(sol)
		