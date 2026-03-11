'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''

def count_char(word:str):
    return [{"char": c, "count": word.count(c)} for c in set(word)]
    
print(count_char("asdqweaswa"))