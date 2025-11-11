'''
複習：
# 定義（設計）
def 功能名(參數):
    # 函式區塊
    return 回傳值


# 使用（call a function）
功能名(引數)       
變數 = 功能名(引數)
'''


'''
Parameter 參數 vs. Argument 引數

Parameter 參數：
在函式定義時出現，用於接收資料的變數


Argument 引數：
在函式被呼叫時，傳入的實際值
'''

def func(a, b):
    return a*10 - b*5

# 主要程式
n1 = 2
n2 = 3

# 位置對應
func(n1, n2)  # a = n1, b = n2 是引數
func(n2, n1)  # a = n2, b = n1

# 關鍵字對應
func(a = n1, b = n2)  
func(b = n2, a = n1)

# 例題
# 

def total(hundreds, tens, ones):
    # return 數字的實際值
    return hundreds*100 + tens*10 + ones

# total(2, 5)   # 十位數為 2，個位數為 5  | return 25
# total(tens=2, ones=5)

# 混用
# total(1, ones=5, tens=6)
# total(ones=5, tens=6, 1)

'''
可變長度參數: *args
特性：接所有的位置對應引數，存在 args 這個變數
args：tuple
print(1)
print(1, 2)


'''

def add_all(*args):
    count = 0
    for num in args:
        count += num
    return count


print(add_all(1))     # args = (1)
print(add_all(1,2))    # args = (1, 2)
print(add_all(1,2,3))  # args = (1, 2, 3)



'''
可變長度參數: **kwargs
特性：接所有的關鍵字對應引數，存在 kwargs 這個變數
kwargs：dict
'''

def info(**kwargs):
    print(kwargs)

info(name='Leo', age=13, color='blue')
info(name='Mary', age=14)
info(name='Amber')



# *args 和 **kwargs 的先後順序
# (*args, **kwargs)


def show(*args, **kwargs):
    print(f"args:{args} | kwargs:{kwargs}")

show('1', 'abc', name='Leo', age=13)
show(1,2)
show(name='Leo', age=13)



# List & Tuple
'''
L = [1,2,3]  # 改
T = (1,2,3)  # 不能改內容

L[0]  # 1
T[0]  # 1

L[1] = 5   # L = [1, 5, 3]
T[1] = 5   # 出錯
'''