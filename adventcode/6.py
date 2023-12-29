file = open("inputs/input_6")
lines = [line.strip() for line in file]
time = int("".join([n for n in lines[0].split(" ") if n.isnumeric()]))
distance = int("".join([n for n in lines[1].split(" ") if n.isnumeric()]))

r = 0
for i in range(time + 1):
    front = i * (time - i)
    if front > distance:
        r = i
        break

print(time + 1 - 2 * r)
