"""
*
Написать программу калькулятор которая предлагает 
ввести пример для решения пока пользователь не введет команду "стоп"
Программа должна решить пример и запросить следующий.
При вводе команды "стоп" программа завершается.
Поддерживаемые операции: + - * ** /
Пример:
    Введите пример или 'стоп' для завершения: 2 + 2
    Ответ: 4
    Введите пример или 'стоп' для завершения: 16 / 8
    Ответ: 2
    Введите пример или 'стоп' для завершения: 1651+
    Неправильный формат. Пример: '2 + 4'


eval() exec() нельзя
"""

tag_stop = "stop"
tag_sum = "+"
tag_sub = "-"
tag_mult = "*"
tag_div = "/"
tag_square = "**"

operations = [tag_sum, tag_sub, tag_div, tag_square, tag_mult]

while True:
    expression = input("input expression " \
                       f"(available operations {" ".join(operations)}, " \
                       f"{tag_stop} for terminate):")

    if (expression.lower() == tag_stop):
        break
    
    args = None
    operation = [o for o in operations if (-1 < expression.find(o))]
    if (0 < len(operation)):
        operation = operation[0]
        args = list(map(str.strip, expression.split(operation)))
        
    if (args and (2 == len(args)) and all(map(str.isdecimal, args))):
        result = None
        args = list(map(int, args))
        if (tag_sum == operation):
            result = sum(args)
        elif (tag_sub == operation):
            result = args[0] - args[1]
        elif (tag_mult == operation):
            result = args[0] * args[1]
        elif (tag_div == operation):
            result = args[0] / args[1]
        elif (tag_square == operation):
            result = args[0] ** args[1]
        print(f"result: {result}")
    else:
        print("wrong input")
        
        
