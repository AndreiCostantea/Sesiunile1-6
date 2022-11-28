# joc de noroc cu zar
# avem un zar cu 6 fete
# trebuie sa scriem un nr si verificam daca nr este egal cu fata zarului aruncat

import random
zar = [1, 2, 3, 4, 5, 6]

diceRoll = random.choice(zar)

numarAles = int(input('Alege un numar: '))

if numarAles < diceRoll:
    print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales {numarAles}, dar a fost {diceRoll}')
elif numarAles > diceRoll:
    print(f'Ai pierdut! Ai ales un numar mai mare. Ai ales {numarAles}, dar a fost {diceRoll}')
else:
    print('Ai castigat! Felicitari!')