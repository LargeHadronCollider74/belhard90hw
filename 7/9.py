# '''

# *
# В структуре данных из 5 урока задание №2 каждому сотруднику
# добавить к параметру "навык" параметр "мастерство" измеряемый от 0 до 100
#
# Написать программу которая анализирует всю структуру данных и выводит сотрудников
# с наибольшим параметром "мастерство" для каждого существующего навыка.
# Пример вывода:
#     1. Python - Иванов - 98
#     2. JS - Петров  - 74
#     3. Базы данных - Николаев - 87
#     ...
#
#
# ** Вывод в консоль организовать в виде таблицы
#    Пример вывода 
#    (перед выводам отсортировать по убыванию "мастерства"):
#
#     --------------------------------------------------
#     | № |   Навык     |       ФИО       | Мастерство |
#     ==================================================
#     | 1 | Python      | Иванов Н.С.     |     98     |
#     | 2 | JS          | Петров В.В.     |     87     |
#     | 3 | Базы данных | Николаев Е.Н.   |     74     |
#     ...
# '''

users = {"Vasya1": {"job_title":"boss",
                     "birth_year":2020,
                     "skills": [{"name":"money", "level":80}]},
         "Vasya2": {"job_title":"manager",
                    "birth_year":2010,
                    "skills": [{"name":"presentations", "level":30}, {"name":"negotiations", "level":50}]},
         "Vasya3": {"job_title":"cleaner",
                    "birth_year":2015,
                    "skills": [{"name":"clean toilets", "level":100}]}
}

header_name = "name"
header_skill = "skill"
header_level = "level"

max_name = len(header_name)
max_skill = len(header_skill)
max_level = len(header_level)

for name, details in users.items():
    top_skill = details["skills"][0]
    for s in details["skills"][1:]:
        if (s["level"] > top_skill["level"]):
            top_skill = s
    details["top_skill"] = top_skill
    if (len(name) > max_name):
        max_name = len(name)
    if (len(details["top_skill"]["name"]) > max_skill):
        max_skill = len(details["top_skill"]["name"])
    if (len(str(details["top_skill"]["level"])) > max_level):
        max_level = len(name)

print_users = dict(sorted(users.items(), key=lambda u: u[1]["top_skill"]["level"])[::-1])

line_len = sum({max_name, max_skill, max_level}) + (4 * 3) + 2
print("-" * line_len)
print(f"| # | {header_skill.center(max_skill)} | {header_name.center(max_name)} | {header_level.center(max_level)} |")
print("=" * line_len)
for i, item in enumerate(print_users.items(), 1):
    print(f"| {i} | {item[1]["top_skill"]["name"].ljust(max_skill)} | {item[0].ljust(max_name)} | {f"{item[1]["top_skill"]["level"]}".ljust(max_level)} |")
print("-" * line_len)

