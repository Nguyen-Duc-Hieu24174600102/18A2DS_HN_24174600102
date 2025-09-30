class Myclass:
    def __init__(self,value):
        self.value=value
    def my_method(self):
        print('Giá trị của đối tượng :',self.value)
 #Tạo một đối tượng từ lớp Myclass
obj = Myclass(50) #Khai báo và khởi tạo đối tượng obj từ lớp Myclass
 #Gọi phương thức my_method() của đối tượng obj
obj.my_method()  