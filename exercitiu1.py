# Pentru un bancomat verificam username-ul si parola
# Userul are doar 2 incercari
# Parola are doar 2 incercari
# Userul doreste sa scoata o anumita suma de bani acesta avand un sold curent
# Suma dorita trebuie sa fie <= decat soldul curent
# Daca introduci o suma prea mare poate sa aleaga daca sa reincerce sau nu
# La a doua incercare daca user-ul pune o suma prea mare iese din program

expectedUser = 'Ion'
expectedPass = '1234'
sold = 500.49

user = input('Introdu userul: ')

if user == expectedUser:
    print('Bine ai venit!')
else:
    print('Username gresit! Incearca din nou!')
    user = input('Introdu userul: ')
    assert user == expectedUser, 'Username incorect. O zi buna!'
    print('User corect!')

parola = input('Introdu parola: ')

if parola == expectedPass:
    print('Parola corecta!')
else:
    print('Parola incorecta! Incearca din nou')
    parola = input('Introdu parola: ')
    assert  parola == expectedPass, 'Parola gresita! O zi frumoasa!'
    print('Parola corecta')

suma = float(input('Introdu suma dorita: '))
if suma <= sold:
    print('Ridicati banii')
else:
    print('Suma dorita este prea mare. Fonduri insuficiente!')
    reincercare = input('Doriti sa incercati din nou? Da/Nu: ')
    if reincercare == 'Da':
        suma = float(input('Introdu suma dorita: '))
        assert suma <= sold, 'Suma introdusa e prea mare'
        print('Ridicati banii')
    elif reincercare == 'Nu':
        print('La revedere!')
    else:
        assert False, 'Eroare'
