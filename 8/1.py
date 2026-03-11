"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""

def ShortName(name:str, revers:bool=False) -> str:

    items = list(map(str.capitalize, name.split()))
    surname = items[0] if (1 <= len(items)) else ""
    firstname = items[1] if (2 <= len(items)) else ""
    middlename = items[2] if (3 <= len(items)) else ""

    result = ""
    if revers:
        result += f"{firstname[0]}." if (firstname) else ""
        if (firstname):
            result += f"{middlename[0]}." if (middlename) else ""
        if (result):
            result += " "
        result += surname
    else:
        result += surname
        if (middlename or firstname):
            result += " "
        result += f"{firstname[0]}." if (firstname) else ""
        result += f"{middlename[0]}." if (middlename) else ""

    return result

print(ShortName("asdas qwe dfdh"))
print(ShortName("asdas qwe dfdh", True))
print(ShortName("asdas qwe ", True))
