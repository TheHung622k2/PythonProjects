


# Chương trình chính
if __name__ == '__main__':
    n = 5
# cách 1:
    s = 0
    for i in range(n+1):
        s += i**2
    print("s = {}".format(s))

# cách 2:
    def Square(x):
        return x**2
    s = 0
    for i in range (n + 1):
        s += Square(i)
    print("s = {}".format(s))

# cách 3:
    s = 0
    for i in range(n + 1):
        x = lambda i : i*i
        s += x(i)
    print("s = {}".format(s))