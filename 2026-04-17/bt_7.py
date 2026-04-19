n = int(input("Nhap n: "))

check = True

while n > 0:
    digit = n % 10
    
    if digit != 6 and digit != 8:
        check = False
        break
    
    n = n // 10

if check == True:
    print("La so may man")
else:
    print("Khong phai so may man")