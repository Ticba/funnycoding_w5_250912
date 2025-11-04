'''
# 定義（設計）
def 功能名(參數):
    # 函式區塊
    return 回傳值


# 使用（call a function）
功能名(引數)       
變數 = 功能名(引數)
'''

# call function
# print()
# int(list)

def 洗手():
    # 函式區塊
    print('濕')
    print('搓')
    print('沖')
    # return 回傳值

print(洗手()) # None: 沒有

def my_max_2():
    return [1, 3]

print(my_max_2(), end='\n')

def my_sum(n1, n2, n3):
    # 參數 parameter：引數丟進來的時候對應到的名字
    # n1 = 3
    # n2 = 4
    # n3 = 5
    result = n1 + n2 + n3
    return result

print(my_sum(3, 4, 5))   # 引數 argument：3, 4, 5
print(my_sum(10, 10, 10))
print(my_sum(1, 9, 10))

# 練習：
# 

def my_average(n1, n2, n3, n4):
    # 回傳 4 個數字的平均
    return int((n1+n2+n3+n4)/4)
    pass

print(my_average(3, 4, 5, 7))    # 預期 5 
print(my_average(10, 10, 10, 30))# 預期 15
print(my_average(1, 9, 10, 4))   # 預期 6


