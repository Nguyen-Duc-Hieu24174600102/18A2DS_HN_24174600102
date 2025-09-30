class Dog:
    """Đại diện cho một con chó với các thuộc tính cơ bản."""
    # Thuộc tính lớp
    DogCount = 0
    species = 'Dog'

    # instance attribute
    def __init__(self, name, size, age, color):
        """
        Khởi tạo một đối tượng Dog mới.
        Tham số:
            name (str): Tên của con chó.
            size (str): Kích thước của con chó (ví dụ: 'Small', 'Medium', 'Large').
            age (int): Tuổi của con chó.
            color (str): Màu sắc của con chó.
        """
        self.name = name   # Thuộc tính đối tượng
        self.size = size
        self.age = age
        self.color = color