import math

inputfile = open('input.txt', 'r')

firstSet = []
secondSet = []

for line in inputfile.readlines():
    firstNumber = int(line.split('   ')[0].strip())
    secondNumber = int(line.split('   ')[1].strip())
    firstSet.append(firstNumber)
    secondSet.append(secondNumber)


firstSet = sorted(firstSet)
secondSet = sorted(secondSet)

totalDistance = 0
for i in range(len(firstSet)):
    x = firstSet[i]
    y = secondSet[i]
    setDistance = math.dist([x], [y])
    totalDistance += setDistance
    print(setDistance)

print(totalDistance)