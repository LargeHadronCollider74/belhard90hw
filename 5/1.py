'''
Дан произвольный список. Вывести на экран в обратном порядке. 
Задачу решить 2мя способами. 
'''

l = [1, 2, 3, 4, 5, 6, 7, 8]

print(f"original list {l}")
print(f"reverse list1 {l[::-1]}")

l.reverse()

print(f"reverse list2 {l}")
