# for n in [0, 1, 2, 3, 4]:   # range(5) => 產生 0, 1, 2, 3, 4
#     print(n)

# 0
# 1
# 2
# 3
# 4

'''
迭代：重複替換



for 變數 in 迭代的東西:
    重複的內容
'''


for i in range(5):   # 先判斷會執行幾次迴圈？ 5 次
    print(i)   # 0, 1, 2, 3, 4

# 輸出偶數
# 0 1 2 3 4
# 0 2 4 6 8



# 輸出奇數
# 1 3 5 7 9
# n*2+1  |  n*2-1

# for n in range(5):
#     print(n*2+1)

# range
'''

'''
# range(開始, 結束, 步伐)
# 開始有包含，結束包含

# range(結束)        等同於   range(0, 結束, 1)
# range(開始, 結束)  等同於   range(開始, 結束, 1)

for n in range(0, 5, 2):
    print(n)  # 0 2 4

for n in range(5, 0, -2):
    print(n)

# 用 range() 的功能輸出奇數
# 想輸出 1 ~ 100 之間的奇數
for n in range(1, 100, 2):
    print(n)

# 任務: 顯示 100 ~ 200 之間 3 的倍數

for n in range(100):
    print(n*2+1)  # n*2+1