f = open("2021\\Day3\\Day3Input.txt", "r")
data = f.read()

numbers = [line for line in data.split()]

f.close()

gammaRate = []
epsilonRate = []

for i in range(len(str(numbers[0]))):
    count0 = 0
    count1 = 0
    for j in range(len(numbers)):
        if numbers[j][i] == "0":
            count0 += 1
        if numbers[j][i] == "1":
            count1 += 1
    if count0 > count1:
        gammaRate.append(0)
        epsilonRate.append(1)
    if count0 < count1:
        gammaRate.append(1)
        epsilonRate.append(0)

print(int("".join(str(x) for x in gammaRate), 2) * int("".join(str(x) for x in epsilonRate), 2))

oxygenArray = numbers
nBinaryDigits = len(numbers[0])
for index in range(nBinaryDigits): 
    cnt = sum(1 if oxy[index]=='1' else -1 for oxy in oxygenArray)
    oxygenArray = list(filter(lambda binary: binary[index]=='1' if cnt>=0 else binary[index]=='0', oxygenArray))
    if len(oxygenArray)==1:
        break  
co2Array = numbers
for index in range(nBinaryDigits):
    cnt = sum(1 if co2[index]=='1' else -1 for co2 in co2Array)
    co2Array = list(filter(lambda binary: binary[index]=='0' if cnt>=0 else binary[index]=='1', co2Array))
    if len(co2Array)==1:
        break
oxygenVal = int(oxygenArray[0], 2)
co2Val = int(co2Array[0], 2)
print(oxygenVal*co2Val)