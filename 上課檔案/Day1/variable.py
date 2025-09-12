#  等號右邊: 運算結果， 等號左邊: 箱子
# x = 10 # 把運算結果存入箱子，箱子 -> Variable 變數

# print(x)
# print(x + 10) # -> 20

# 變數可以存什麼？ 什麼都可以存

# 1. Integer

y = 20
print("type of y:",type(y))
# 2. Floating point number

z = 20.0
print("type of z:",type(z))

# 3. String 

s = '20'  # "" ''
print("type of s:",type(s))

# 4. List 串列  形式：[1, 'hi', 123]      # split() 產生的結果是一個串列

my_list = []               # 空的串列
my_list2 = [1, 'hi', 123]  # 三節車廂的串列
print("type of my_list2:",type(my_list2))

# List 串列可以存放不同類型的資料
# split() 產生串列裡面都是 str   ex: '123 456' -> split() -> ['123', '456']
