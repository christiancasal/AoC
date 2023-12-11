gamesfile = open('games.txt', 'r')

redThreshold = 12
greenThreshold = 13
blueThreshold = 14

invalidBucket = []

totalPossibleValidGames = range(1,101)
sumOfValidGames = 0
for n in totalPossibleValidGames:
    print(n)
    sumOfValidGames = sumOfValidGames + n


for line in gamesfile.readlines():
    game = line.split(':')
    gameId = game[0].split(' ')[1]

    elfGame = game[1].split(';')

    for eg in elfGame:
       cube = eg.split(',')

       for c in cube:
           numberColor = c.strip().split(' ')
           number = int(numberColor[0])
           color = numberColor[1]
           
           if (number > redThreshold and color == 'red') or (number > greenThreshold and color == 'green') or (number > blueThreshold and color == 'blue'):  
            #    print('Game ' + gameId + ' is not valid')
               invalidBucket.append(int(gameId))
               break
               

    # print(elfGame)

invalidBucket = list(set(invalidBucket))
invalidBucket.sort()

print('Total possible valid games: ' + str(sumOfValidGames))
print('Total invalid games: ' + str(sum(invalidBucket)))
print('Total valid games: ' + str(sumOfValidGames - sum(invalidBucket)))

gamesfile.close()