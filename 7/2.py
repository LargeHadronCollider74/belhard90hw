'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

original = list()
while True:
    original.clear()
    original.extend(input("Input 3 words:").split())
    if (3 != len(original)):
        print("3 words!!!!")
        continue
    break

tagret = list()
for word in original:
    tagret.append("".join(char * i for i, char in enumerate(word, 1)))
    
print(f"Original: {original}")
print(f"Target: {tagret}")
print(" ".join(tagret))

