import random
num = random.randrange(1,100)
for x in range(1,7):
    a = int(input('Guess a number b/w 1 to 100: '))
    if(a == num):
        print('you have won the game. ')
    elif(a < num):
        print('guess a higher number: ')
    elif(a > num):
        print('guess a lower number: ')
    else: 
        print('better luck next time')        
        