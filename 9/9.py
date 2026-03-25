"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""

def dict_from_args(*args, **kwargs) -> dict:
    result = dict()

    if all([isinstance(v, int) for v in args]):
        result["args_sum"] = sum(args)
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми")

    if all([isinstance(v, str) for v in kwargs.values()]):
        result["kwargs_max_len"] = max([len(v) for v in kwargs.values()])
    else:
        raise TypeError("Все аргументы - ключевые слова должны быть строками")
        
    return result

print(dict_from_args(3,45,6,True, a="zczx", b="asde18497bxzkjh"))