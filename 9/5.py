'''
*
Написать рекурсивную функцию, которая принимает список 
и печатает каждых элемент на новой строке. 
Если элемент списка - список, то его элементы должны выводиться 
с отступом относительно родительского на 2 символа. 
Символ для отступа передать дополнительными необязательным параметром.

** написать такую же функцию но без рекурсии

Пример1: some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
1
2
3
--4
----5
----6
--7
8
9

Пример2: some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
1
--2
------3
----4
5
------6
------7
8
--------9
--------10
----11
12




'''

def print_list(l:list, indent_char:str="=="):
    
    def print_list_internal(l:list, indent_level:int):
        # nonlocal indent_char
        for i in l:
            if not isinstance(i, list):
                print(indent_char * indent_level, i, sep="")
            else:
                print_list_internal(i, indent_level + 1)
            # print_list_internal(i, indent_level + 1) if isinstance(i, list) else print(indent_char * indent_level, i, sep="")
                
    print_list_internal(l, 0)
    
some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
print_list(some_list)    
    
some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
print_list(some_list)    

