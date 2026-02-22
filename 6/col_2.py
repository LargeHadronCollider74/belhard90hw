"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
    
    ** задать вопрос о желании добавить сотрудника,
        если ответ да - добавить сотрудника через несколько input
        (после добавления сотрудника вывести всю структуру консоль)

"""

from pprint import pprint

users = {"Vasya1": {"job_title":"boss",
                     "birth_year":2020,
                     "skills": ["money"],
                     "childrens": [{"name":"Vasya1 junior", "birth_year":2024}]},
         "Vasya2": {"job_title":"manager",
                    "birth_year":2010,
                    "skills": ["presentations", "negotiations"],
                    "childrens": [{"name":"Vasya2 junior", "birth_year":2023}]},
         "Vasya3": {"job_title":"cleaner",
                    "birth_year":2015,
                    "skills": ["clean toilets"],
                    "childrens": [{"name":"Vasya3_1", "birth_year":2024},
                                  {"name":"Vasya3_2", "birth_year":2023}]}
}

pprint(users);

normalized_names = dict(zip(map(str.lower, users.keys()), users.keys()))

name = input("input user name: ")
if name.lower() in normalized_names.keys():
    pprint(users[normalized_names[name.lower()]])
else:
    if "Y" == input(f"User \"{name}\" not found, enter Y to add:"):
      job_title = input(f"User \"{name}\" job title:")
      birth_year = int(input(f"User \"{name}\" birth year:"))
      skills = list(input(f"User \"{name}\" skills (space separated):").split())
      childrens = input(f"User \"{name}\" childrens (sequence of name and birth year comma separated):")
      childrens = list(map(str.split, childrens.split(",")))
      childrens = list({"name": child_name, "birth_year": child_birth_year} for child_name, child_birth_year in childrens)
      new_user = dict([(name, {"job_title": job_title,
                               "birth_year": birth_year,
                               "skills": skills,
                               "childrens": childrens})])
      pprint(new_user)
      users.update(new_user)
      pprint(users)
