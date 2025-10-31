my_list = [3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
# 串列的操作
# 1. 取用 indexing
# 2. 新增 item    -> .append()
# 3. 刪除 item    -> .pop()
# 4. 數 item 有重複幾個 -> .count(item)
# 5. 排順序 -> .sort()
# 6. 翻轉   -> .reverse()

item = 11
my_list.append(item)  # 新增 item 到最後
print(my_list)

# 排順序
# 1. 3 4 5 1 2
my_list = []
for i in range(5):
    item = int(input())
    my_list.append(item)
# my_list: [3, 4, 5]
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)
