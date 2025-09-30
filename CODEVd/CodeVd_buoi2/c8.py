class Dog:
    """
    Minh họa lớp Dog với các thuộc tính protected
    """
    _DogCount = 0   # protected: thuộc tính LỚP (giao diện protected)

    def __init__(self, name: str, size: str, age: int):
        self._name = name    # protected: thuộc tính protected (theo quy ước)
        Dog._DogCount += 1   # tăng thuộc tính lớp

    def _display(self):  # Phương thức protected
        print(f"Name is {self._name}")