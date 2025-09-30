# Khai báo lớp chim
class Bird:
    def flight(self):  # Định nghĩa phương thức flight()
        print("Many birds can fly")

# Khai báo lớp chim sẽ kế thừa từ lớp Bird
class Sparrow(Bird):
    def flight(self):  # Ghi đè phương thức flight()
        print("Sparrows can fly")

# Khai báo lớp Đà điểu kế thừa từ lớp Bird
class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly")

obj1 = Bird()
obj2 = Sparrow()
obj3 = Ostrich()

obj1.flight()
obj2.flight()
obj3.flight()