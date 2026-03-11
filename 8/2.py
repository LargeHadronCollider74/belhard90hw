'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

def SquareInfo(dimensions:tuple[int, int], perimeter:bool=False) -> int:
    w, h = dimensions
    return (2 * w) + (2 * h) if (perimeter) else w * h

dim = (10, 20)
print(f"Square {SquareInfo(dim)}")
print(f"Perimeter {SquareInfo(dim, True)}")
