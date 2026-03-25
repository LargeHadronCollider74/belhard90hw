'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''

def TypeFilter(l:list, t:type=str) -> list:
    return list(filter(lambda v: isinstance(v, t), l))

l = [13, "asdasd", False, ["qwe", (4, True)]]

print(TypeFilter(l, str))
print(TypeFilter(l, list))
print(TypeFilter(l, bool))
