#輸入 John Mary Steve David
#輸出
# John
# Mary
# Steve
# David

x = input()   # x= 'John Mary Steve David'
x_split = x.split() # x_split -> ['John', 'Mary', 'Steve', 'David']
print(x_split[0])
print(x_split[1])




print(*x_split, sep='\n')  # 1 個串列
# *串列   |  *元組
# x_split -> ['John', 'Mary', 'Steve', 'David']  1 個串列
# *x_split -> 'John', 'Mary', 'Steve', 'David'   4 個字串