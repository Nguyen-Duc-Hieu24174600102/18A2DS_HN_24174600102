class Stack:
    def __init__(self, size):
        self.size = size
        self.data = []
    
    def push(self, value):
        if self.is_full():
            print("Ngăn xếp đầy!")
        else:
            self.data.append(value)
    
    def pop(self):
        if self.is_empty():
            print("Ngăn xếp rỗng!")
        else:
            return self.data.pop()
    
    def is_empty(self):
        return len(self.data) == 0
    
    def is_full(self):
        return len(self.data) == self.size


if __name__ == "__main__":
    st = Stack(3)
    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)   # báo đầy
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())  # báo rỗng