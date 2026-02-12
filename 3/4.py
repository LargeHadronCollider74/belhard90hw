n = int(input("input number: "))
print(f">>> {n}")
print(f"тыс: {str(int(n / 1000))}")
n %= 1000
print(f"сот: {str(int(n / 100))}")
n %= 100
print(f"дес: {str(int(n / 10))}")
n %= 10
print(f"ед: {str(n)}")
