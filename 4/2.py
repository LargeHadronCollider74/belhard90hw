import math

numbers = input("type numbers:")
numbers = list(map(float, numbers.split()))
print(f"array: {numbers}")
print(f"result: sum - {sum(numbers)}, max - {max(numbers)}, avg - {sum(numbers) / len(numbers)}")

