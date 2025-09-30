class LopCha:
    def __init__(self, ten_cha):
        self.ten_cha = ten_cha

    def thong_tin(self):
        print("Tôi là Lớp Cha, tên của tôi là", self.ten_cha)


class LopCon(LopCha):
    def __init__(self, ten_cha, ten_con):
        # Gọi hàm khởi tạo của lớp cha để khởi tạo các thuộc tính từ lớp cha
        super().__init__(ten_cha)
        self.ten_con = ten_con

    def thong_tin(self):
        print("Tôi là Lớp Con, tên của tôi là", self.ten_con)
        # Gọi phương thức của lớp cha bằng cách sử dụng super()
        super().thong_tin()


class LopChau(LopCon):
    def __init__(self, ten_cha, ten_con, ten_chau):
        # Gọi hàm khởi tạo của LopCha và LopCon để khởi tạo các thuộc tính
        # LớpChau kế thừa LopCon
        super().__init__(ten_cha, ten_con)
        self.ten_chau = ten_chau

    def thong_tin(self):
        print("Tôi là Lớp Cháu, tên của tôi là", self.ten_chau)
        # Gọi phương thức của LopCon
        super().thong_tin()


# Sử dụng các lớp
lop_chau = LopChau("Ông A", "Bác B", "Cháu C")
lop_chau.thong_tin()