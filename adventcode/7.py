file = open("inputs/input_7")
lines = [line.strip() for line in file]
dico = {}
for el in lines:
    dico[el.split(' ')[1]] = el.split(' ')[0]
for k,v in dico.items():
    print(k, v)

# trier les main par rapport a leur force d'abord.

# compter les ocurrences de cartes de chaque main.
occ_1 = {}
occ_ = {}
occ_dico = {}
occ_dico = {}
occ_dico = {}
occ_list = []
for values in dico.values():
    occ = []
    for el in set(values):
        occ.append(values.count(el))
    occ_list.append(sorted(occ))

key_list = [n for n in dico.keys()]
val_list =  [n for n in dico.values()]
i = 0
for occurrences in occ_list:
    if 5 in occurrences:
        occ_dico[key_list[i]]= [val_list[i], 6]
    elif 4 in occurrences:
        occ_dico[key_list[i]]= [val_list[i], 5]
    elif 3 in occurrences and 2 in occurrences:
        occ_dico[key_list[i]]= [val_list[i], 4]
    elif 3 in occurrences: 
        occ_dico[key_list[i]]= [val_list[i], 3]
    elif 2 in occurrences:
        n = 0
        for el in occurrences:
            if el == 2:
                n += 1
        if n == 2:
            occ_dico[key_list[i]]= [val_list[i], 2]
        else:
            occ_dico[key_list[i]]= [val_list[i], 1]
    else:
        occ_dico[key_list[i]]= [val_list[i], 0]
    i += 1

sorted = []
for i in range(7):
    for k, v in occ_dico.items():
        if v[-1] == i:
            sorted.append([k, v[0]])

order = [2, 3, 4, 5, 6, 7 ,8, 9, T, G, Q, A]

print(sorted)
