# function 的預設參數值

# type_op: '+'  default: n1=0, n2=0
# n1 + n2 

# type_op: '-'
# n1 - n2

def op(type_op, n1, n2):  # 先寫不需要 default value 的參數，再寫有 default value 的參數。
    if type_op == '+':
        return n1+n2
    elif type_op == '-':
        return n1-n2
    else:
        print('wrong')
        return None

print(op('+', 2, 3))
print(op('-', 2, 3))
# print(op('+'))
# print(op('-'))
print(op())


# 題目
#
'''


'''
def passed(score, thershold = 60):
    # 回傳值為 bool -> True/False
    pass

print(passed(73, 50)) # True/False
print(passed(80))
print(passed(80, 90))