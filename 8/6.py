"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""

def yes_or_no(numbers: list) -> str:
    
    if not all([n.is_integer() for n in numbers]):
        return "False"
    
    result = ["yes" if v in numbers[:i] else "no" for i, v in enumerate(numbers)]

    return f"{result}"

print(yes_or_no([11,2,3,4,11,23,6]))
print(yes_or_no([11,2,3.01,4,11,23,6]))
