f = open("2021\\Day2\\Day2Input.txt", "r")
data = f.read()

commands = [line for line in data.split("\n")]

f.close()

# part 1
horizontalPosition = 0
verticalPosition = 0
for command in commands:
    details = command.split(' ')
    if details[0] == 'forward':
        horizontalPosition += int(details[1])
    if details[0] == 'down':
        verticalPosition -= int(details[1])
    if details[0] == 'up':
        verticalPosition += int(details[1])

print(abs(verticalPosition * horizontalPosition))

# part 2

horizontalPosition2 = 0
verticalPosition2 = 0
aim = 0
for command in commands:
    details = command.split(' ')
    if details[0] == 'forward':
        horizontalPosition2 += int(details[1])
        verticalPosition2 += aim * int(details[1])
    if details[0] == 'down':
        aim -= int(details[1])
    if details[0] == 'up':
        aim += int(details[1])

print(abs(horizontalPosition2 * verticalPosition2))