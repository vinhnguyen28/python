n = int(input("Nhap n: "))

a = 0
b = 1

print(a, end=" ")
print(b, end=" ")

while True:
    c = a + b
    
    if c > n:
        break
    
    print(c, end=" ")
    
    a = b
    b = c