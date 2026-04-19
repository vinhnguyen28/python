n = int(input("Nhap n: "))

tong = 0
tich = 1

while n > 0:
    digit = n % 10
    
    tong = tong + digit
    tich = tich * digit
    
    n = n // 10

print("Tong =", tong)
print("Tich =", tich)