# class 類別

int   # +, -, /, %
str   # +, *

list  # .append(), .sort()

# 發明 python 的人他寫的，他用 c 語言寫出來的



class Person:
    def __init__(self, height, weight):  # 初始化 method (function)
        self.height = height
        self.weight = weight
    
    def show_my_info(self):
        print("---", self.height, self.weight, "---")

p1 = Person(160, 50)  # 創一個 Person 類型的物件   => Person.__init__(Person, height, weight)
p2 = Person(180, 78)
p1.show_my_info()
p2.show_my_info()