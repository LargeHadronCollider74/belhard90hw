'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Алфавит считаем от 0. a-0, b-1, c-3 и т.д.
Например: 13520 -> bdfca.
'''

repl =  "abcdefghij"
number = ""

while True:
    number = input("Input number:")
    if (number.isnumeric()):
        break
    print(f"\"{number}\"' is not a number!")

# word = ""
# for n in number:
#     word += repl[int(n)]
word = "".join(repl[int(n)] for n in number)

print(f"Result: {word}")


