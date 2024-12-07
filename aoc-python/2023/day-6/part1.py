import re
inputfile = open('input.txt', 'r')

lines = []
for line in inputfile.readlines():
	foo = line.strip().splitlines()
	print(foo)

# print(lines[0])


# print(lines)
inputfile.close()