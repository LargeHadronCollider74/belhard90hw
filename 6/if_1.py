"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""

age = int(input("age:"))

match age:
    case n if n < 12: status = "child"
    case n if n < 18: status = "teenager"
    case n if n < 25: status = "youth"
    case n if n < 45: status = "in one's prime"
    case n if n < 65: status = "senior"
    case _: status = "oldy"

print(f"age: {age}, state: {status}")
