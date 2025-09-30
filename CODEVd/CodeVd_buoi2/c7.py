class Dog:
    DogCount = 0   # Thuộc tính của lớp

    def __init__(self, name, size, age, color):
        self.name = name   # Thuộc tính đối tượng
        self.size = size   # Thuộc tính đối tượng
        self.age = age     # Thuộc tính đối tượng
        self.color = color # Thuộc tính đối tượng
        Dog.DogCount += 1  # Tăng bộ đếm (số lượng chó) lên 1 mỗi khi có đối tượng mới được tạo

    # Instance method: Phương thức đối tượng (dùng self)
    def show_count_instance(self):
        print(f"Số lượng đối tượng Dog đã được tạo [instance method] = {Dog.DogCount}")

    # Class method: Phương thức lớp (dùng cls)
    @classmethod
    def show_count_class(cls):
        print(f"Số lượng đối tượng Dog đã được tạo [class method] = {cls.DogCount}")

    # Static method: Phương thức tĩnh (không dùng self hay cls)
    @staticmethod
    def show_count_static():
        print(f"Số lượng đối tượng Dog đã được tạo [static method] = {Dog.DogCount}")