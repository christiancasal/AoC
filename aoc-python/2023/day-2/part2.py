gamesfile = open('games.txt', 'r')

redThreshold = 12
greenThreshold = 13
blueThreshold = 14

productBucket = []

totalPossibleValidGames = range(1,101)
sumOfValidGames = 0
for n in totalPossibleValidGames:
    print(n)
    sumOfValidGames = sumOfValidGames + n


for line in gamesfile.readlines():
    game = line.split(':')
    gameId = game[0].split(' ')[1]

    elfGame = game[1].split(';')
    print('GAME:', elfGame)

    redMin = 0
    greenMin = 0
    blueMin = 0

    for eg in elfGame:
       cube = eg.split(',')

       for c in cube:
           numberColor = c.strip().split(' ')
           number = int(numberColor[0])
           color = numberColor[1]

           if (number > redMin and color == 'red'):
                redMin = number
           if (number > greenMin and color == 'green'): 
                greenMin = number
           if (number > blueMin and color == 'blue'):  
                blueMin = number
           
    print('REDMIN:', redMin)
    print('GREENMIN:', greenMin)
    print('BLUEMIN:', blueMin)
               
    productBucket.append(redMin * greenMin * blueMin)

print('Sum of Powers: ' + str(sum(productBucket)))

gamesfile.close()