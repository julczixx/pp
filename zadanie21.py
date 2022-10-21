odpowiedz = input('Guess the number from the dice:')
import random
prawidlowaodpowiedz = random.randrange(1,6)
if odpowiedz == prawidlowaodpowiedz:
    print('Correct!')
else:
        print('not correct')