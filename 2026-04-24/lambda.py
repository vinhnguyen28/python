
# câu a trị tuyệt đối
print("\ncau a : tri tuyet doi")
trituyetdoi = lambda so: so if so >= 0 else -so
so = int(input("Nhap so n cho cau a: "))
print("Ket qua: (tri tuyet doi):", trituyetdoi(so))

# Câu b: tính giá trị n + 15
print("\ncau b: tinhs gia tri n + 15")
cong15 = lambda so: so + 15
so = int(input("Nhap so n cho cau b: "))
print("Ket qua: (n + 15):", cong15(so))

# Câu c : tích 2 số x và y
print("\ncau c: tinh 2 so x va y")
ttich = lambda so1, so2: so1 * so2
so1 = int(input("Nhap so thu nhat (x): "))
so2 = int(input("Nhap so thu hai (y): "))
print("Ket qua : (tich x * y):", ttich(so1, so2))

# Câu d: kiểm tra bội của 13 và 19
print("\ncau d: kiem tra boi cua 13 va 19")
kiemtra = lambda so: (so % 13 == 0 or so % 19 == 0)
so = int(input("Nhap so n cho cau d: "))
if kiemtra(so):
    print("n la boi cua 13 hoac 19")
else:
    print("n khong phai boi cua 13 hoac 19")



# câu e: tính diện tích hình tròn 
print("\ncau e: tinh dien tich hinh tron")
dientichtron = lambda r: 3.14 * r * r
r = float(input("Nhap ban kinh r: "))
print("Ket qua cau e (dien tich hinh tron):", dientichtron(r))


#câu f:tính chu vi hình chữ nhật 
print("\ncau f : tinh chu vi hinh chu nhat")
chuvihcn = lambda dai, rong: 2 * (dai + rong)
dai = float(input("Nhap chieu dai: "))
rong = float(input("Nhap chieu rong: "))
print("Ket qua cau f (chu vi HCN):", chuvihcn(dai, rong))


# Cau g: Kiểm tra số chính phương
print("\ncau g: kiem tra so chinh phuon")
ktchinhphuong = lambda n: int(n**0.5) * int(n**0.5) == n
n = int(input("Nhap so n: "))
if ktchinhphuong(n):
    print("Ket qua cau g: n la so chinh phuong")
else:
    print("Ket qua cau g: n khong phai so chinh phuong")


# câu H: kiểm tra số nguyên tố 
print("\ncau h: kiem tra so nguyen to")
ktnguyento = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
n = int(input("Nhap so n: "))
if ktnguyento(n):
    print("Ket qua cau h: n la so nguyen to")
else:
    print("Ket qua cau h: n khong phai so nguyen to")

# câu i : kiểm tra tam giác 
print("\ncau i: kiem tra tam gia")
kttamgiac = lambda a, b, c: (
    "khong phai tam giac" if (a + b <= c or a + c <= b or b + c <= a)
    else "tam giac deu" if (a == b == c)
    else "tam giac can" if (a == b or a == c or b == c)
    else "tam giac vuong" if (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a)
    else "tam giac thuong"
)

a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))

print("Ket qua cau i:", kttamgiac(a, b, c))