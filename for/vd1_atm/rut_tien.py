# câu a
while True:
    m = int(input("nhập số tiền cần rút:"))
    if m <= 0 or m % 5 != 0:
        print("số tiền không thỏa mãn.")
    else:
        break

# lưu lại số tiền ban đầu
m1 = m

soTo100 = m // 100 # chia lấy phần nguyên
m = m % 100 # số tiền còn lại
soTo20 = m // 20
m = m % 20
soTo5 = m / 5

print("phương án rút tiền tốt nhất:")
print("{} tờ 100 + {} tờ 20 + {} tờ 5".format(soTo100, soTo20, soTo5))

print()

# câu b
m = m1 # lấy lại số tiền lúc đầu
soCach = 0
for soTo100 in range(m // 100 + 1):
    for soTo20 in range(m // 20 + 1):
        for soTo5 in range(m // 5 + 1):
            if soTo100 * 100 + soTo20 * 20 + soTo5 * 5 == m1:
                soCach += 1
                print("{}: {} tờ 100 + {} tờ 20 + {} tờ 5.".format(soCach, soTo100, soTo20, soTo5))
print("Có tất cả {} cách rút".format(soCach))
