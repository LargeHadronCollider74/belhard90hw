'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''

# set1 = {*map(int, input("input numbers (space separated)1:").split())}
# set2 = {*map(int, input("input numbers (space separated)2:").split())}
# set3 = {*map(int, input("input numbers (space separated)3:").split())}
set1 = {1, 2, 11, 22}
set2 = {1, 2, 22, 33}
set3 = {1, 2, 33, 44}
print(set1, set2, set3, sep="\n")

uniq_set = set1 | set2 | set3
print(f"Uniq numbers: {uniq_set}")

common_set = set1 & set2 & set3
print(f"Common numbers: {common_set}")

pairs = (set1 & set2) | (set1 & set3) | (set2 & set3)
print(f"Total uniq numbers: {uniq_set.difference(pairs)}")
