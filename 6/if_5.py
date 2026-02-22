'''
Запросить число от 1 до 12. 
Если ввели другое число сообщить об ошибке. 
Если ввели не число сообщить об ошибке. 
Когда введут допустимое число - вывести на экран соответствующее 
название месяца, пору года и сколько дней в данном месяце.

'''

monthes = [
    {"name": "January", "max": 31 },
    {"name": "February", "max": 28 },
    {"name": "March", "max": 31 },
    {"name": "April", "max": 30 },
    {"name": "May", "max": 31 },
    {"name": "June", "max": 30 },
    {"name": "July", "max": 31 },
    {"name": "August", "max": 31 },
    {"name": "September", "max": 30 },
    {"name": "October", "max": 31 },
    {"name": "November", "max": 30 },
    {"name": "December", "max": 31 },
]

month = input("specify month number:")
if (month.isdecimal()):
    month = int(month)
    if (1 <= month <= 12):
        print(monthes[month - 1])
    else:
        print("wrong month number")
else:
    print("is not a number")