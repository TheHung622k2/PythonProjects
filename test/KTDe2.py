import datetime
class Xe:
    sonamluuhanhtoida=20

    # hàm thiết lập (constructor)
    def __init__(self, bienso, hangsx, namsx):
        self.bienso = bienso
        self.hangsx = hangsx
        self.namsx = namsx

    def nhap_thong_tin_xe(self):
        self.bienso = input("nhap bien so xe: ")
        self.hangsx = input("nhap hang san xuat: ")
        self.namsx = input("nhap nam san xuat: ")

    def xuat_thong_tin_xe(self):
        print("Bien so: " + self.bienso)
        print("Hang san xuat: " + self.hangsx)
        print("Nam san xuat: " + str(self.namsx))
        print("So nam luu hanh: " + str(self.sonamluuhanhtoida))

    def tinh_so_nam_luu_hanh(self):
        return datetime.datetime.now().year - self.namsx
    
if __name__ == '__main__':
    danh_sach_xe = []

    n = int(input("nhap so luong xe: "))
    
    if n < 0 or n >= 100:
        print("so luong xe khong hop le!")
    
    for i in range(n):
        print("nhap thong tin cho xe thu {i+1}:")
        bienso = input("nhap bien so xe: ")
        hangsx = input("nhap hang san xuat: ")
        namsx = int(input("nhap nam san xuat: "))
        danh_sach_xe.append(Xe(bienso, hangsx, namsx))



    
    

    

    


    