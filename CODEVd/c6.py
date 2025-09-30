class Dog: 
    DogCount = 0           # Thuộc tính lớp 
    def __init__(self, name, size, age, color): 
        self.name = name   # Thuộc tính đối tượng 
        self.size = size   # 
        self.color = color # 
        Dog.DogCount += 1  #    
     
    @staticmethod 
    def Report(): 
       print("Tổng số  đối tượng Dog:{}".format(Dog.DogCount)) 
 
# Tạo các đối tượng Dog 
dog1 = Dog("Buddy", "Medium", 5, "Brown") 
dog2 = Dog("Max", "Small", 3, "Black") 
 
# Sử dụng phương thức tĩnh Report() để lấy số lượng đối tượng đã được tạo 
dog1.Report() 