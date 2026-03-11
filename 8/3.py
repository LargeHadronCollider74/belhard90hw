'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''

def f(value:int) -> int:
    result = 1
    for v in range(1, value + 1):
        result *= v
    return result

print(f"f: {f(5)}")
