
"""
Viết chương trình cho người dùng nhập 1 chuỗi (S) và 1 từ (word).
 Đếm xem trong S có bao nhiêu từ word.
"""

import string

s = input("Nhập chuỗi S: ")
word = input("Nhập từ cần đếm: ")

s = s.lower()
word = word.lower()

for dau in string.punctuation:
    s = s.replace(dau, "")

ds = s.split()

count = 0
for i in ds:
    if i == word:
        count = count + 1

print("Số từ", word, "là:", count)