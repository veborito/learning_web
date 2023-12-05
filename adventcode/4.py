file = open("inputs/input_4")
lines = [line.strip()[10:].split('|') for line in file]
pairs = []
for line in lines:
    pairs.append([line[0].split(' '), line[1].split(' ')])
for pair in pairs:
    for el in pair:
        for n in pair:
            for s in n:
                if s == " " or s == "":
                    n.remove(s)
new_cards = []
match = []


def number_occ(cards,  card):
    nb = 0
    for w in range(len(cards)):
        if cards[w] == card:
            nb += 1
    return nb


for x in range(len(pairs)):
    print(f"x -> {x}")
    matches = 0
    occ = 0
    new_cards.append(pairs[x])
    for i in range(len(pairs[x][0])):
        for j in range(len(pairs[x][1])):
            if pairs[x][0][i] == pairs[x][1][j]:
                matches += 1
    if matches > 0:
        occ = number_occ(new_cards, pairs[x])
        print(f"matches : {matches}")
        print(f"occurences : {occ}")
        y = 0
        while y < occ:
            for k in range(x + 1, x + matches + 1):
                new_cards.append(pairs[k])
            y += 1
        print(len(new_cards))
print(len(new_cards))