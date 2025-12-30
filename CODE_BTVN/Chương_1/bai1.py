class HinhChuNhat:
    def __init__(self, dai=0, rong=0):
        self.dai = dai
        self.rong = rong

    def nhap(self):
        self.dai = float(input("Nhập chiều dài: "))
        self.rong = float(input("Nhập chiều rộng: "))

    def chu_vi(self):
        return 2 * (self.dai + self.rong)

    def dien_tich(self):
        return self.dai * self.rong

    def xuat(self):
        print(f"Hình chữ nhật: dài = {self.dai}, rộng = {self.rong}")
        print(f"Chu vi = {self.chu_vi()}")
        print(f"Diện tích = {self.dien_tich()}")


if __name__ == "__main__":
    hcn = HinhChuNhat()
    hcn.nhap()
    hcn.xuat()