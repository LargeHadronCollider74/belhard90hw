'''
Буква "a" стоит 10 очков, "b" - 20, "c" - 30, "d" - 40
Запросить кодовою фразу из пяти символов используя только a, b, c, d.
Вывести на экран общее количество очков введенной фразы.

'''

legal = "abcd"
cost = {"a": 10, "b": 20, "c": 30, "d": 40}

phrase = input(f"input phrase (legal chars only [{legal}]):")

test = list(map(legal.count, phrase))

if sum(test) != len(test):
    print("illegal chars found")
else:
    print(f"Sum: {sum(map(cost.get, phrase))}")
