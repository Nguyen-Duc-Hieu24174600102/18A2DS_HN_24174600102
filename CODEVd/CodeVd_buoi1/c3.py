class Dog: 
    #Constructor có tham số 
    def __init__(self, name): 
        print('Đây là constructor có tham số.') 
        self.name=name 
     
    def display(self): 
        print("Hello",self.name) 
 
bull = Dog("The Dom") 
bull.display()           