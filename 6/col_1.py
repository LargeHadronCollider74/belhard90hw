"""
Запросить трижды ввод наименования товаров и их цену через пробел. 
"пример: 
>>>яблоко 10"
>>>груша 15
>>>малина 20
    
    - создать из введенных данных словарь где ключ это наименование, а цена значение
    - запросить имя товара, найти его в словаре, и вывести его цену, увеличенную на 15%. 
    - вывести сумму всех товаров

"""
products = {}
print("input products: '<product_name> <product_price>'")

name, price = input(">>1: ").split()
products[name] = int(price)
name, price = input(">>2: ").split()
products[name] = int(price)
name, price = input(">>3: ").split()
products[name] = int(price)

print("products:", products, sep="\n")

name = input("input product name: ")
print(f"product \"{name}\": {1.3 * products.get(name, 0):.2f}")

print(f"product total price: {sum(products.values())}")
