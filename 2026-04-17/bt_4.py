n = int(input("Nhap n: "))

chan = 0
le = 0

while n > 0:
    digit = n % 10
    
    if digit % 2 == 0:
        chan = chan + 1
    else:
        le = le + 1
    
    n = n // 10

print("So chu so chan:", chan)
print("So chu so le:", le)