"""
Написать функцию print_n() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
какой раз по счету выполняется эта функция. 

"""

def print_n(*args, itetarion:int = 1, **kwargs):
    if (100 < itetarion):
        return
    print(f"iteration: {itetarion} ->", *args, **kwargs)
    print_n(*args, itetarion = itetarion + 1, **kwargs)

print_n(123, "asd")
