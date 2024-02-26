# Nhập 1 số nguyên n (0 < n <= 1000)
while True:
        n = int(input("Nhập một số nguyên n (0 < n <= 1000)"))
        if 0 < n <= 1000:
            break
        
# a) Kiểm tra n có phải số nguyên tố?
# B1: Define a func checking a number is a SNT
def LaSNT(n):
      if n < 2:
            return False
      for i in range(2, n//2 + 1): # từ 2 -> n/2
          if n % i == 0:
                return False
      return True

if LaSNT(n):
      print("{} là số nguyên tố".format(n))
else:
      print("{} không phải là số nguyên tố".format(n))

# b) In ra các SNT <= n
print("Các SNT <= {}".format(n))
for i in range(2, n + 1):
      if LaSNT(i):
            print("%5d" % i, end=" ")
        