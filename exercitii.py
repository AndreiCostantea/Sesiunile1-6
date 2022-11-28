# def contBancar(userName, parola, plata):
#     i = 0
#     while i < 3:
#         if userName == 'Costantea Andrei':
#             if parola == '2424':
#                 if plata <= 200:
#                     print('Tranzactie reusita')
#                     break
#                 else:
#                     print('Fonduri insuficiente!')
#                     break
#             else:
#                 print('Parola gresita!')
#                 parola = input('Parola: ')
#                 i += 1
#         else:
#             print('Username gresit!')
#             userName = input('ID: ')
#             i += 1
#     print('Multumim! O zi frumoasa')
#
# contBancar(input('ID: '), input('Parola: '), int(input('Sold: ')))

def bubblesort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# listaSortata = bubblesort([3, 6, 8, 1, 4, 9, 0, 10])
# print(listaSortata)

# def listaMax(lista):
#     listaSortata = bubblesort(lista)
#     return listaSortata[-1]
# maxim = listaMax([3, 6, 8, 1, 4, 9, 0, 10])
# print(maxim)

# def listaMax2(lista):
#     maxim = 0
#     for i in range(len(lista)):
#         if maxim < lista[i]:
#             maxim = lista[i]
#     return maxim
# maxim = listaMax2([3, 6, 8, 1, 4, 9, 0, 10])
# print(maxim)
import random

def diceRoll():
    zar = [1, 2, 3, 4, 5, 6]
    numarZar = random.choice(zar)
    numarAles = int(input('Alege un numar: '))
    if numarAles < numarZar:
        print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales {numarAles}, dar a fost {numarZar}')
    elif numarAles > numarZar:
        print(f'Ai pierdut! Ai ales un numar mai mare. Ai ales {numarAles}, dar a fost {numarZar}')
    else:
        print('Ai castigat! Felicitari!')

diceRoll()
diceRoll()
diceRoll()
diceRoll()
diceRoll()
diceRoll()
diceRoll()