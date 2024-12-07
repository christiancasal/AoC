import re
inputfile = open('input.txt', 'r')

schematics = []
symbolizedDigits = []

# matricize the input
def findAdjecency(currentRow, startingPosition, digit):
	# print(currentRow," ", startingPosition)

	adjecentPostions = []

	for position, value in enumerate(digit):
		adjecentPostions.append([currentRow - 1, startingPosition + position])
		adjecentPostions.append([currentRow + 1, startingPosition + position])
	

	if(startingPosition == 0):
		adjecentPostions.append([currentRow, len(digit)])
		adjecentPostions.append([currentRow - 1, len(digit)])
		adjecentPostions.append([currentRow + 1, len(digit)])
	elif ((len(digit) + startingPosition) == 140):
		adjecentPostions.append([currentRow, startingPosition - 1])
		adjecentPostions.append([currentRow - 1, startingPosition - 1])
		adjecentPostions.append([currentRow + 1, startingPosition - 1])
	else:
		adjecentPostions.append([currentRow, startingPosition - 1])
		adjecentPostions.append([currentRow - 1, startingPosition - 1])
		adjecentPostions.append([currentRow + 1, startingPosition - 1])
		adjecentPostions.append([currentRow, startingPosition + len(digit)])
		adjecentPostions.append([currentRow - 1, startingPosition + len(digit)])
		adjecentPostions.append([currentRow + 1, startingPosition + len(digit)])

	# print(adjecentPostions)
	return adjecentPostions

for line in inputfile.readlines():
	schematics.append(line.strip())


for row, schematic in enumerate(schematics):
	digits = re.findall( '(\d+)', schematic )
	# print(digits)

	digitBucket = []
	symbolBucket = []
	for digit in digits:
		findPosition = schematic.find(digit)
		coordinates = findAdjecency(row, findPosition, digit)
		for coordinate in coordinates:
			# print(coordinate)
			symbol = schematics[coordinate[0]][coordinate[1]]
			# if(row == 44 and digit == '641'):
			# 	print(digit)
			if(symbol != '.'):
				# print(symbol)
				symbolBucket.append(symbol)
				digitBucket.append(int(digit))
				symbolizedDigits.append(int(digit))
		
		if(len(digit) == 1): 
			schematic = schematic.replace(str(digit), '.', 1)
		if(len(digit) == 2):
			schematic = schematic.replace(str(digit), '..', 1)
		if(len(digit) == 3):
			schematic = schematic.replace(str(digit), '...', 1)
	
	# if(row == 44):
	# 	print("row: " + str(row) + ' ' + str(digitBucket))
	# print(row)
	# print(schematic)
	
# get all possible numbers
# print(symbolizedDigits)
# print(len(symbolizedDigits))
uniqueSymbolizedDigits = list(set(symbolizedDigits))
print('Sum of Digits: ' + str(sum(symbolizedDigits)))

inputfile.close()