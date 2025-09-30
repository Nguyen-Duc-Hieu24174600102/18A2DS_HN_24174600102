class Zebra:  # Lớp cha1
    def __init__(self):
        print("Zebra")

    def Display(self):
        print("I'm a zebra")


class Donkey:  # Lớp cha2
    def __init__(self):
        print("Donkey")

    def Display(self):
        print("I'm a donkey")


class Zonkey(Zebra, Donkey):  # Lớp con Zonkey kế thừa lớp cha1, cha2
    def __init__(self):
        Zebra.__init__(self)
        Donkey.__init__(self)
        print("Zonkey")


obj = Zonkey()
obj.Display()  # có vấn đề phát sinh khi chạy phương thức này!