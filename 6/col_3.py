"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

from pprint import pprint

d = {'one':11, 'two':22, 'hello':'python', True:False}

pprint(d)

del_index = int(input("input item index fo delete:"))

del_key = list(d.keys())[del_index]

del d[del_key]

pprint(d)
