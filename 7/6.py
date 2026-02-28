"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""

stop_tag = "stop"
sep = ":"
d = dict()

while True:
    value = input(f"Input <username>{sep} <review> ({stop_tag} for terminate):")
    if (value.lower() == stop_tag):
        break
    pos = value.find(sep)
    if (-1 == pos):
        print("wrong input")
        continue
    name, review = value[:pos].strip(), value[pos + 1:].strip()
    if (" " in name):
        print("wrong input")
        continue
    d[name] = review
    
print(f"review count: {len(d)}")
print(f"users: {", ".join(d.keys())}")
print(f"reviews:", *d.values(), sep="\n")
