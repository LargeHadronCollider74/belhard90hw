'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

n1, n2, n3 = list(map(int, input("input 3 numbers, space separated:").split()))

max_val = None

if (n1 > n2) and (n1 > n3):
    max_val = n1
elif (n2 > n1) and (n2 > n3):
    max_val = n2
elif (n3 > n1) and (n3 > n2):
    max_val = n3
    
print(f"Max {max_val}")
