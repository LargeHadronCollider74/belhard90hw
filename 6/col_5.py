"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""

# sentence = input("type sentence:")
sentence = "asd qwe zxc asd asdasdasdasdqwekzhxvkals"

words = sentence.split()
print(f"Uniq words count: {len(dict.fromkeys(words))}" )

symbols = list(dict.fromkeys(sentence).keys())
symbols_inline = "".join(symbols)
print(f"Uniq symbols count: {len(symbols)}" )

symbols_count = list(map(sentence.count, symbols_inline))
max_value = max(symbols_count);
max_index = symbols_count.index(max_value)

print(f"Most symbol {symbols[max_index]}, count {max_value}")
