'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def f(value:int) -> int: return value * f(value - 1) if value else 1

print(f"f: {f(5)}")
