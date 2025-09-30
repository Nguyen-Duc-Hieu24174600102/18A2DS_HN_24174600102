class Dog:
# Thuộc tính lớp
    DogCount = 0
    species = 'Dog'
# instance attribute
    def __init__(self, name, size, age, color):
        self.name = name # Thuộc tính đối tượng
        self.size = size
        self.age = age
        self.color = color
#instance của lớp Dog
obj1 = Dog("Buddy", "Medium", 5, "Brown")
obj2 = Dog("Max", "Small", 3, "Black")
#Truy cập thuộc tính lớp
print("obj1 is a {}".format(obj1.__class__.species))
print("obj2 is also a {}".format(obj2.__class__.species))
#Truy cập thuộc tính của instance
print("{} is {} years old".format(obj1.name, obj1.age))
print("{} is {} years old".format(obj2.name, obj2.age))