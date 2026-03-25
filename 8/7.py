"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""

def RowInfoDict(row:str) -> dict:
    result = {}
    result["symols"] = sum(1 for c in row if c.isprintable())
    result["words"] = len(row.split())
    result["rows"] = len(row.split("\n"))
    result["sentences"] = len(row.split("."))
    return result

def RowInfoView(data:dict) -> str:
    return f"Symols count = {data["symols"]}, " \
           f"Words count = {data["words"]}, " \
           f"Rows count = {data["rows"]}, " \
           f"Sentences count = {data["sentences"]}"

row = "row:str asd q8e\n9712 sad\nowieur asdaf. lkajsd wqeruy"
row_dict = RowInfoDict(row)
print(row, row_dict, RowInfoView(row_dict), sep="\n")