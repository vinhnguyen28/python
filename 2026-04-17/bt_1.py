a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

for i in range(a, b + 1):
    if i % 3 == 0:
        continue
    
    print(i, end=" ")