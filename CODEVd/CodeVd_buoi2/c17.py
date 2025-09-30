from abc import ABC, abstractmethod

# Tạo lớp trừu tượng 'Animal' với phương thức trừu tượng 'Say'
class Animal(ABC):
    @abstractmethod
    def Say(self):
        pass

# Tạo lớp con 'Dog' kế thừa từ 'Animal'
class Dog(Animal):
    def Say(self):
        print("Whoooopp whooooppp...")

# Tạo lớp con 'Cat' kế thừa từ 'Animal'
class Cat(Animal):
    def Say(self):
        print("Meooo meooo")

    # Định nghĩa một phương thức 'Jump' cho lớp 'Cat'
    def Jump(self):
        print("I'm jumping up high")

# Khởi tạo đối tượng từ lớp 'Dog'
obj_dog = Dog()
# Gọi phương thức 'Say' của đối tượng 'obj_dog'
obj_dog.Say()

# Khởi tạo đối tượng từ lớp 'Cat'
obj_cat = Cat()
# Gọi phương thức 'Say' của đối tượng 'obj_cat'
obj_cat.Say()
