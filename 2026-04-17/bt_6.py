n = int(input("Nhap n: "))

max_digit = 0

while n > 0:
    digit = n % 10
    
    if digit > max_digit:
        max_digit = digit
    
    n = n // 10

print("Chu so lon nhat:", max_digit)