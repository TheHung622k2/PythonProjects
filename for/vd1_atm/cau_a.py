while True:
    m = int(input("nhập số tiền cần rút:"))
    if m <= 0 or m % 5 != 0:
        print("số tiền không thỏa mãn.")
    else:
        break

soTo100 = m // 100 # chia lấy phần nguyên
m = m % 100 # số tiền còn lại
soTo20 = m // 20
m = m % 20
soTo5 = m / 5

print("phương án rút tiền tốt nhất:")
print("{} tờ 100 + {} tờ 20 + {} tờ 5".format(soTo100, soTo20, soTo5))
