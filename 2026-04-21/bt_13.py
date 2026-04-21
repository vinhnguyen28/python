s = input()

s = s.strip()

while "  " in s:
    s = s.replace("  ", " ")

s = s.replace(" ,", ",")
s = s.replace(" .", ".")

ds = s.split("\n")

kq = []
for dong in ds:
    dong = dong.strip()
    kq.append(dong)

print("\n".join(kq))