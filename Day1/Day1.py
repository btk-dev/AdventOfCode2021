f = open("2021\\Day1\\Day1Input.txt", "r")
data = f.read()

numbers = [int(line) for line in data.split()]

f.close()

myNumbers = []

for number in numbers:
    myNumbers.append(number)

increased = 0
increased2 = 0

for i in range(1, len(myNumbers)):
    if myNumbers[i] > myNumbers[i-1]:
        increased += 1

originalSum = myNumbers[0] * myNumbers[1] * myNumbers[2]
for i in range(2, len(myNumbers)):
    newSum = myNumbers[i-2] * myNumbers[i-1] * myNumbers[i]
    if newSum > originalSum:
        increased2 += 1
    originalSum = newSum

print(increased)
print(increased2)