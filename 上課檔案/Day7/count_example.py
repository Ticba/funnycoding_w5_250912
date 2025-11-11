# dict
# 新增 (V)
# 刪除
# 插入
# 修改 (V)



# 例子：多行輸入，輸入水果，EOF結尾
# 

fruits = {}
while True:
    try:
        fruit = input()
        if fruit not in fruits.keys():
            fruits[fruit] = 0
        fruits[fruit] += 1
    except:
        break

print(fruits)