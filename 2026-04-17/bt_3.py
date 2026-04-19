n = int(input("Nhap n: "))

for i in range(11, n + 1):
    s = str(i)
    
    ok = True
    
    for j in s:
        if j != s[0]:
            ok = False
            break
    
    if ok == True:
        print(i, end=" ")