set1 = {'opel', 'volvo', 2, 3, 4}
set2 = {'opel', 'audi', 5, 6}
print(set1)

print(set1.intersection(set2))
print(set1.difference(set2))

set1.update([5, 6, 7, 8])
print(set1)
print(type(set1))

setnou = set()
setnou.update({2, 3, 4, 5, 2})
print(setnou)
setnou.add(3)
print(setnou)