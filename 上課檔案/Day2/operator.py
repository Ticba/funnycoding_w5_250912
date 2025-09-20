# 運算子 operator
# 運算元 operand

# 算數運算子 num op num -> num
'''
運算子 +, -, *, /, //, %
運算元 連接在運算子兩側的值

運算元為 int ， 意義上是加法
print(123 + 345) # -> 468

5 除以 3 的商數是 1 ，餘數是 2
print(5//3)   # 5 除以 3 取商數
print(5%3)    # 5 除以 3 取餘數


str + str -> str
str * num -> str

運算元為 str 
print('123' + '345') # -> '123345'  ，串接
print('123' * 2)     # -> '123123'  ，重複

運算元為 list
list + list -> list
list * num  -> list

a_list = [1, 2, 3]
print(a_list + a_list) # [1, 2, 3, 1, 2, 3] 串接
print(a_list * 2)      # [1, 2, 3, 1, 2, 3] 重複
'''







# 比較運算子  oprand op oprand -> True/False (bool)
'''
運算子 > | < | >= | <= | == 相等 | != 不相等
1 < 2    # True
3 >= 4   # False
# >= 中間沒有空格，代表它是一個運算子

5 == 5   # True
13 != 6  # True

print(5 == 5)

print('ss' != 'ss')  # str == str ，用來判斷字串相等
'''

# 
'''
運算子 and 都 | or 或 | not 不
# and 兩邊都是 True 才會是 True
print(True and True)  # True
print(True and False) # False
print(False and True) # False
print(False and False)# False

# or 兩邊有 True 就會是 True
print(True or True)  # True
print(True or False) # True
print(False or True) # True
print(False or False)# False


# not 單（一）元運算子   not True/False
print(not True)     # False
print(not False)    # True
'''

# 分數 >= 60 且 缺席 < 2 次 -> pass
score = 20
absent = 18
print(score >= 60 and absent < 2)

# 複合運算
#   = : 賦（予）值運算子
#   +=  | *=  | -=
# x = 5
# # x -= 1   # x = x - 1
# x + 1
# print("x:", x)

x = 10
x %= 2
print(x)


