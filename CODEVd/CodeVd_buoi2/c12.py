class Animal:
    """ Lớp cơ sở (lớp cha)"""
    def __init__(self, name):
        self._name = name

    def Display(self):        # Hiển thị tên con vật
        print("I'm {}".format(self._name))


class Dog(Animal):
    """ Lớp dẫn xuất (lớp con)"""
    def __init__(self, name, size, age, color):  # Khởi tạo lớp con
        super().__init__(name)   # Gọi hàm khởi tạo của lớp cha
        self.size = size
        self.age = age
        self.color = color

    def Go(self, place):         # Phương thức riêng của lớp con
        print("I'm going to {}".format(place))