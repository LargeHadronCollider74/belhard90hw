'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******

* - елочка со снегом
'''

height_min = 3
height_max = 20

height = 0

while True:
    height = int(input(f"Christmas tree height [{height_min}...{height_max}]:"))
    if ((height >= height_min) and (height <= height_max)):
        break
    print("Wrong height!")

for l in range(0, height):
   # spaces = " " * (height - l)
   # print(f"{spaces}{"*" * ((2 * l) + 1)}")
   print(f"{"*" * ((2 * l) + 1)}".rjust(height + l + 1))

line_len = (2 * height) + 3
print(f"{"-" * (line_len + 2)}")
print(f"|{"^".center(line_len)}|")

for l in range(0, height):
   print(f"|{f"^{"*" * ((2 * l) + 1)}^".center(line_len)}|")

print(f"{"-" * (line_len + 2)}")

