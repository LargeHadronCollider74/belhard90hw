"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""

min_num = 10
value = None

while True:
    value = input(f"Input mumber not less {min_num}:")
    if (not value.isnumeric()):
        print("is not a number")
        continue
    if (min_num <= int(value)):
        break
    print("wrong number")
    
result = 0
for c in value:
    n = int(c)
    result += n * n

print(f"result: {result}")
