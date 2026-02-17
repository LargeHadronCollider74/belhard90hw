import datetime
macro = "Юзер с именем {0} заходил на сайт в {1:02}:{2:02}"
username = input("user name:")
now = datetime.datetime.now()
print(macro.format(username, now.hour, now.minute))

