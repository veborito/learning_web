file = open("inputs/input_5")
lines = [line.strip() for line in file]
seeds = [int(n) for n in lines[0][7:].split(' ')]
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temp = []
temp_to_hum = []
hum_to_loc = []

i = 0
falg = 0
for line in lines:
    if line == "seed-to-soil map:":
        falg = 1
    if line == "soil-to-fertilizer map:":
        falg = 2
    if line == "fertilizer-to-water map:":
        falg = 3
    if line == "water-to-light map:":
        falg = 4
    if line == "light-to-temperature map:":
        falg = 5
    if line == "temperature-to-humidity map:":
        falg = 6
    if line == "humidity-to-location map:":
        falg = 7
    if falg == 1:
        seed_to_soil.append(lines[i].split(' '))
    if falg == 2:
        soil_to_fertilizer.append(lines[i].split(' '))
    if falg == 3:
        fertilizer_to_water.append(lines[i].split(' '))
    if falg == 4:
        water_to_light.append(lines[i].split(' '))
    if falg == 5:
        light_to_temp.append(lines[i].split(' '))
    if falg == 6:
        temp_to_hum.append(lines[i].split(' '))
    if falg == 7:
        hum_to_loc.append(lines[i].split(' '))
    i += 1

new_seed = []
for i in range(0, len(seeds), 2):
    new_seed.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

seed_to_soil = [[int(n) for n in line] for line in seed_to_soil[1:-1]]
soil_to_fertilizer = [[int(n) for n in line] for line in soil_to_fertilizer[1:-1]]
fertilizer_to_water = [[int(n) for n in line] for line in fertilizer_to_water[1:-1]]
water_to_light = [[int(n) for n in line] for line in water_to_light[1:-1]]
light_to_temp = [[int(n) for n in line] for line in light_to_temp[1:-1]]
temp_to_hum = [[int(n) for n in line] for line in temp_to_hum[1:-1]]
hum_to_loc = [[int(n) for n in line] for line in hum_to_loc[1:]]

def convert_le_bail(sources, dest):
    range_list = []
    for source in sources:
        convert = 0
        low_end = source[0]
        high_end = source[1]
        for conv in dest:
            if low_end < conv[1] < high_end < (conv[1] + conv[2]):
                convert = 1
                s1 = conv[1] - conv[1] + conv[0]
                s2 = high_end - conv[1] + conv[0]
                range_list.append((s1, s2))
            elif low_end < conv[1] < (conv[1] + conv[2]) < high_end:
                convert = 1
                s1 = conv[0]
                s2 = conv[2] + conv[0]
                range_list.append((s1, s2))

            elif low_end > conv[1] < (conv[1] + conv[2]) > high_end:
                convert = 1
                s1 = low_end - conv[1] + conv[0]
                s2 = high_end - conv[1] + conv[0]
                range_list.append((s1, s2))

            elif conv[1] < low_end < (conv[1] + conv[2]) < high_end:
                convert = 1
                s1 = low_end - conv[1] + conv[0]
                s2 = conv[2] + conv[0]
                range_list.append((s1, s2))
        if convert == 0:
            range_list.append((low_end, high_end))
    return range_list
print(new_seed)
soil = convert_le_bail(new_seed, seed_to_soil)
print(soil)
fertilizer = convert_le_bail(soil, soil_to_fertilizer)
print(fertilizer)
water = convert_le_bail(fertilizer, fertilizer_to_water)
print(water)
light = convert_le_bail(water, water_to_light)
print(light)
temperature = convert_le_bail(light, light_to_temp)
print(temperature)
humidity = convert_le_bail(temperature, temp_to_hum)
print(humidity)
location = convert_le_bail(humidity, hum_to_loc)
print(location)

min = 1283471247182947890123748901743890127348
for el in location:
    if el[0] < min and el[0] != 0:
        min = el[0]
print(min)