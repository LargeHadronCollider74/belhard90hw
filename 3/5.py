t = int(input("input total seconds: "))

h = int(t / 3600)
m = int((t % 3600) / 60)
s = int(t % 60)

print(f"{t} -> {h:02d}:{m:02d}:{s:02d}")
print(str(t) + " -> " + "{:02d}".format(h) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
