
# câu a trị tuyệt đối
hamtrituyetdoi = lambda so: so if so >= 0 else -so

so = int(input("Nhap so n cho cau a: "))
print("Ket qua: (tri tuyet doi):", hamtrituyetdoi(so))

# Câu b: tính giá trị n + 15
hamcong15 = lambda so: so + 15
so = int(input("\nNhap so n cho cau b: "))
print("Ket qua: (n + 15):", hamcong15(so))

# Câu c : tích 2 số x và y
hamtich = lambda so1, so2: so1 * so2
so1 = int(input("\nNhap so thu nhat (x): "))
so2 = int(input("Nhap so thu hai (y): "))
print("Ket qua : (tich x * y):", hamtich(so1, so2))

# Câu d: kiểm tra bội của 13 và 19
hamkiemtra = lambda so: (so % 13 == 0 or so % 19 == 0)
so = int(input("\nNhap so n cho cau d: "))
if hamkiemtra(so):
    print("n la boi cua 13 hoac 19")
else:
    print("n khong phai boi cua 13 hoac 19")