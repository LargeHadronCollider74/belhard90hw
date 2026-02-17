print(type(print))
print(1 in [10, 20, 1])
l = [10, 20, 1]
l.insert(-1, 2)
print(2 in l)
print(l)
l[2] = 111
print(l)
print(type(max))
l.remove(20)
print(l)
print(l.pop(1))
print(l)
t = (10, 20, 1)
print(2 in t)
# t[2] = 123123
print(t[2])
s = "qwertyuiop"
print(s[::-1])
print(s[-2:2:-1])

t = "str \"{:*>20}\" num {:010.2f}"
print(t.format("zsdf", 34))
print(t.format("zsdf", 3412396))

t = tuple([1,2,3,78])
print(t)
m = map(str, t)
print(m)
l = list(m)
print(l)
print(type(repr("asd")))
print(type(repr(123456)))
