# number = int(input("type number:"))
number = 12365498745
print(f"{number} => {number:_} => {repr(f"{number:_}").replace("_", " ").replace("'", "")} => {repr(f"{number:_}").translate(str.maketrans({ "_": " ", "'": "" }))}")
