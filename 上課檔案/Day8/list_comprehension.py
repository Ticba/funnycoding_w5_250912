#   串列推導式 list comprehension
#   [表達式 for 元素 in 可迭代物件 if 條件]
#   
# for 元素 in 可迭代物件：
# 元素驗票

# if 條件：
# 驗票成功

# 表達式：
# 穿戴識別證、換裝


'''
Docstring for 上課檔案.Day8.list_comprehension
L = [(i+2) for i in range(5)]
print(L)

# 從 2 到 100 的偶數陣列
# 有 50 個
# range(50) -> [0,1,2,...., 49]
L = [(i*2+2) for i in range(50)]
print(L)

#   搭配 if 使用
L = [i for i in range(101) if i%2==0]
print(L)
'''



#   [表達式 for 元素1 in 可迭代物件 for 元素2 in 可迭代物件]

'''L = []
for i in range(10):
    for j in range(10):
        L.append((i,j))

L = [(i,j) for i in range(10) for j in range(10)]
print(L)
'''


# review dictionary
#d = {"A": 10, "B":11}
#print(d["A"])

# dict comprehension
# dict 的元素：  ？ key:value
'''names = ['Leo', "Amber"]
scores = [90, 95]

d = {name:score for name, score in zip(names, scores)}
print(d)'''

# review tuple
# 有效率的 list 
# 語法 my_tuple = (1,2,3,4)
# 取用 my_tuple[0] => 取用到 1

# 跟 list 不一樣在於不能改
# my_tuple[0] = 0 (X)

# tuple comprehension
t = tuple((i,j) for i in range(10) for j in range(10))
print(t)