"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""

from pprint import pprint

users = [{"name":"u1", "login":"login1", "password":"12" },
         {"name":"u2", "login":"loGin_1", "password":"some_password" },
         {"name":"u3", "login":"loGin#1", "password":"123796" },
         {"name":"u4", "login":"лагін90", "password":"sdf" },
         {"name":"u5", "login":"logиn", "password":"zxlvjlasjd" },
         {"name":"u6", "login":"log2", "password":"asdf" },
         {"name":"u7", "login":"%login", "password":"asdlkj" },
         {"name":"u8", "login":"some_login", "password":"asdasddfa" }]

def WeakPassword(users:list, weak_len:int=5) -> list:
    return list(filter(lambda u: weak_len > len(u["password"]), users))

def ValidLogin(users:list) -> list:
    allowed1 = "qwertyuiopasdfghjklzxcvbnm"
    allowed2 = "1234567890"
    allowed3 = "_"
    return list(filter(lambda u: all([c in allowed1 + allowed2 + allowed3 for c in u["login"].lower()]) and
                                 any([c in allowed1 for c in u["login"]]) and
                                 any([c in allowed2 for c in u["login"]]) and
                                 any([c in allowed3 for c in u["login"]]), users))

pprint(f"Users {users}")
pprint(f"Weak password {WeakPassword(users)}")
pprint(f"Valid logins {ValidLogin(users)}")
