'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''

target = 'Вася'

names = list()

names.append(input("name1: "))
names.append(input("name2: "))
names.append(input("name3: "))
names.append(input("name4: "))
names.append(input("name5: "))

names.sort()

print("sorted names:")
print(*names, sep="\n")
print(f"has a target name \"{target}\": {target in names}")
