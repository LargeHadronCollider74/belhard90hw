"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

a1 = 12.3
a2 = 12.1
a3 = 12.3
a4 = 3.2

all_float = False
has_string = False
has_int_pair = False

if (all([type(a1) == float, type(a2) == float, type(a3) == float, type(a4) == float])):
    all_float = True
elif (any([type(a1) == str, type(a2) == str, type(a3) == str, type(a4) == str])):
    has_string = True
elif ((type(a1) == int) and (type(a3) == int)) or ((type(a2) == int) and (type(a4) == int)) or ((type(a3) == int) and (type(a4) == int)):
    has_int_pair = True

if (all_float or has_string or has_int_pair):
    print(True)
    
    