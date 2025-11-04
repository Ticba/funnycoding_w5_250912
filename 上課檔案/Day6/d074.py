x = int(input())
y = list( map (int,input().split()) )  # 最後還想要是以 list 的方式儲存的話要記得 list() 
# y = input().split()
# #目的：list 的每個 item 都轉成整數
# for i, item in enumerate(y):
#     # i 索引值
#     # item 元素
#     y[i] = int(item)  # str -> int

print(max(y))


# map (int, 什麼東西)
# 做什麼事情：function  例如：int() ，生活化的類子：洗手  濕搓沖捧擦
# 什麼東西：list -> 所有 item 都執行前面那件事情
