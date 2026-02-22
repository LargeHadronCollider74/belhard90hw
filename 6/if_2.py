'''
запросить у пользователя логин пароль и возраст
вывести доступ разрешен:
    логин:admin   пароль:123456    возраст: любой    
    логин:vasya   пароль: vas123   возраст: менее 60
    логин:guest   пароль: любой    возраст:более 18
    
в остальных случаях - "доступ запрещен".

'''

inhibit = "access denied"
grant = "access granted"

users = {
    "admin": {"password":"123456", "age":None},
    "vasya": {"password":"vas123", "age":{"value":60, "less":True}},
    "guest": {"password":None, "age":{"value":18, "more":True}}
}

login, password, age = input("specify <login> <password> <age>:").split()
age = int(age)

details = users.get(login)

success = False

if details:
    if (None == details.get("password")) or (password == details.get("password")):
        if (None == details.get("age")):
            success = True
        elif (details.get("age").get("less") and (age < details.get("age").get("value"))):
            success = True
        elif (details.get("age").get("more") and (age > details.get("age").get("value"))):
            success = True

print(grant if success else inhibit)
