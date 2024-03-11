# cách 1
a = [1, 2, 3, 4]
b = []
for i in range(len(a)):
    b.append(a[i]**2)
print(b)

# cách 2
# định nghĩa hàm bình phương
def Square(x):
    return x**2
b = map(Square,a) # áp dụng hàm Square() cho mỗi phần tử trong danh sách a, tạo ra một đối tượng map chứa các kết quả sau khi hàm Square() được áp dụng
b = list(b) # do trả về một object nên phải ép kiếu để chuyển thành list
print(b)

# cách 3
b = list(map(lambda x : x ** 2, a))
print(b)