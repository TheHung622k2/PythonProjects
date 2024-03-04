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
b = map(Square,a) 
b = list(b) # trả về Object nên phải ép kiếu
print(b)

# cách 3
b = list(map(lambda x : x ** 2, a))
print(b)