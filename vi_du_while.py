# Cách 1:
print("Sử dụng while")
i = 1
while i <= 100:
    if i % 2 != 0:
        i += 1
    print("%d" % i)
    i += 1

print("Sử dụng for")
# Cách 2:
for i in range(1, 101):
    if i % 2 != 0:
        continue
    print("{}".format(i))