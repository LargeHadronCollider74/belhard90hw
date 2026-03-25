"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""

temp = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

temp_lo_hi = dict(sorted(temp.items(), key=lambda i:i[1]))
# temp_hi_lo = dict(sorted(temp.items(), key=lambda i:i[1])[::-1])
temp_hi_lo = dict(sorted(temp.items(), key=lambda i:i[1], reverse=True))

print(f"original: {temp}")
print(f"lo to hi: {temp_lo_hi}")
print(f"hi to lo: {temp_hi_lo}")
