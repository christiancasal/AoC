import re
inputfile = open('input.txt', 'r')

cards = []
for line in inputfile.readlines():
	cards.append(line.strip().split(': '))

values = []
for card in cards:
	values.append(card[1].split('|'))

scratch_card_dictionary = {}
for card_id, value in enumerate(values):
	winning_number = set(re.findall( '(\d+)', value[0]))
	users_number = set(re.findall( '(\d+)', value[1]))

	users_winning_number_count = len(winning_number.intersection(users_number))

	if(users_winning_number_count > 0):
		for winning_count in range(0, users_winning_number_count):
			index = card_id + 1 + winning_count + 1
			print(winning_count)
			if(index not in scratch_card_dictionary):
				print(scratch_card_dictionary)
				scratch_card_dictionary[index] = 1
			else:
				scratch_card_dictionary[index] += 1
			


print(scratch_card_dictionary)

inputfile.close()