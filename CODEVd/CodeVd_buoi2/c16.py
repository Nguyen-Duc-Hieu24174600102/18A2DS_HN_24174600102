class Airplane:
    """Một lớp đại diện cho máy bay"""
    def fly(self):
        print("Airplane is flying")  # Phương thức fly() trong lớp Airplane

class Superman:
    """Một lớp đại diện cho Superman"""
    def fly(self):
        print("Superman is flying")  # Phương thức fly() trong lớp Superman

def let_it_fly(obj):  # Hàm chấp nhận bất kỳ đối tượng nào
    obj.fly()         # chỉ cần có phương thức fly()

let_it_fly(Airplane())  # Gọi hàm với một đối tượng Airplane
let_it_fly(Superman())  # Gọi hàm với một đối tượng Superman
