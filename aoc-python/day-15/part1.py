inputfile = open('input.txt', 'r')

read = inputfile.read()

values = read.split(',')

currentValue = 0
bucket = []
for v in values:
	for letter in v:	
		currentValue = currentValue + ord(letter)
		currentValue = currentValue * 17
		currentValue = currentValue % 256
	
	bucket.append(currentValue)
	currentValue = 0

print(sum(bucket))

inputfile.close()