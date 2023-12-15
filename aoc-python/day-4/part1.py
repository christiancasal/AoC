import re
inputfile = open('input.txt', 'r')

cards = []
for line in inputfile.readlines():
	cards.append(line.strip().split(': '))

values = []
for card in cards:
	values.append(card[1].split('|'))

points = []
for i, value in enumerate(values):
	winning_number = set(re.findall( '(\d+)', value[0]))
	users_number = set( re.findall( '(\d+)', value[1]))

	users_winning_number_count = len(winning_number.intersection(users_number))

	if(users_winning_number_count > 0):
		points.append(2 ** (users_winning_number_count - 1))

print(sum(points))

inputfile.close()