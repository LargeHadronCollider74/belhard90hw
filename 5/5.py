'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''

find = 'xerox'
replace = 'indesit'

l = ['samsung', 'lg', 'xerox', 'bosch']
pos = l.index('xerox')

print(f"original: {l}")

del l[pos]

print(f"cleared of \"{find}\" (was on position {pos}): {l}")

l.insert(pos, replace)

print(f"\"{replace}\" inserted: {l}")
