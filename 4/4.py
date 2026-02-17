s = "имя: Дмитрий, фамилия: Иванов, возраст: 18"
param_value = list(map(lambda s: list(map(str.strip, s.split(":"))), map(str.strip, s.split(","))))

name = None
surname = None
age = None

for key, val in param_value:
  if key == "имя":
      name = val
  if key == "фамилия":
      surname = val
  if key == "возраст":
      age = val
      
print(f"- {name}", f"- {surname}", f"- {age}", sep = "\n")

