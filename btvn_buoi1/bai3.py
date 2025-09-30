import math

class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        while self.mau == 0:
            print("Mẫu số phải khác 0!")
            self.mau = int(input("Nhập mẫu số: "))

    def rut_gon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def xuat(self):
        self.rut_gon()
        print(f"Phân số = {self.tu}/{self.mau}")


if __name__ == "__main__":
    ps = PhanSo()
    ps.nhap()
    ps.xuat()