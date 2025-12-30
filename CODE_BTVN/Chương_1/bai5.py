class Stack:
    def __init__(self, size):
        self.size = size
        self.data = []
        self.count = 0
    
    def push(self, value):
        if self.is_full():
            print("Ngăn xếp đầy!")
        else:
            self.data.append(value)
            self.count += 1
    
    def pop(self):
        if self.is_empty():
            print("Ngăn xếp rỗng!")
        else:
            self.count -= 1
            return self.data.pop()
    
    def is_empty(self):
        return self.count == 0
    
    def is_full(self):
        return self.count == self.size
    
    def get_count(self):
        return self.count


if __name__ == "__main__":
    st = Stack(3)
    st.push(5)
    st.push(15)
    st.push(25)
    print("Số phần tử trong stack:", st.get_count())
    st.pop()
    print("Số phần tử trong stack:", st.get_count())