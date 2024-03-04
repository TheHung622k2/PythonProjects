def LaSNT(n):
    if n < 2: return False
    for i in range(2, n//2 + 1):
        if n % i == 0: return False
    return True

def InSNT(n):
    for i in range (2, n + 1):
        if (LaSNT(i)):
            print(i, end= ' ')


# def TimSNT(n):
#     while True:
#         if LaSNT(n + 1):
#             print(n + 1)
#             break
#         else:
#             n += 1
            

def TimSNT(n):
    i = n + 1
    while not LaSNT(i):
        i += 1
    return i


# chương trình chính
if __name__ == '__main__':
    n = 11
    print(LaSNT(n))
    print("các số nguyên tố <= %d là " % (n))
    InSNT(n)
    print("\nsố nguyên tố nhỏ nhất > {} là {}".format(n, TimSNT(n)))