class Dog: 
    '''Ví dụ: Minh họa các hàm thuộc tính lớp tích hợp.''' 
    def  __init__(self, name, size, age, color):  
        self.name = name # object attributes  
        self.size = size # object attributes  
        self.age = age # object attributes  
        self.color = color # object attributes 
  
    def display_details(self): 
        print("Name:%s, size:%s, age:%d, color:%s" %     
             (self.name, self.size,self.age, 
self.color)) 
  
bull = Dog("Dom", "large", 2, "yelow") 
print(bull.__doc__) 
print(bull.__dict__) 
print(bull.__module__)