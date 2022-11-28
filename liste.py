primaLista = [1, 2, 3, 'avion', 'miscare', 23]

print(primaLista)
print(len(primaLista))
# daca vren sa dam remove punem itemul din liste nu index-ul lui
primaLista.remove(1)
print(primaLista)

# putem si cu index asa:
primaLista.remove(primaLista[0])
print(primaLista)

primaLista.pop(0)
print(primaLista)

primaLista.extend([1, 2, 3, 4])
print(primaLista)

primaLista = primaLista + [1, 2, 3, 4]
print(primaLista)

primaLista.append('catel')
print(primaLista)

primaLista.insert(2, 2)
print(primaLista)

lista2 = [7, 7, 7]

lista2.extend(primaLista)
print(lista2)

lista2.insert(3, primaLista)
print(lista2)