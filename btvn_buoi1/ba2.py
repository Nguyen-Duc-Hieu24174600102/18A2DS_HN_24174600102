class ThiSinh:
    def __init__(self, hoten="", toan=0, ly=0, hoa=0):
        self.hoten = hoten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa

    def nhap(self):
        self.hoten = input("Nhập họ tên thí sinh: ")
        self.toan = float(input("Điểm Toán: "))
        self.ly = float(input("Điểm Lý: "))
        self.hoa = float(input("Điểm Hóa: "))

    def tong_diem(self):
        return self.toan + self.ly + self.hoa

    def xuat(self):
        print(f"Thí sinh: {self.hoten}, Toán: {self.toan}, Lý: {self.ly}, Hóa: {self.hoa}, Tổng: {self.tong_diem()}")


if __name__ == "__main__":
    n = int(input("Nhập số lượng thí sinh: "))
    ds = []
    for _ in range(n):
        ts = ThiSinh()
        ts.nhap()
        ds.append(ts)

    diem_chuan = 20
    print("\nDanh sách trúng tuyển:")
    for ts in ds:
        if ts.tong_diem() >= diem_chuan:
            ts.xuat()