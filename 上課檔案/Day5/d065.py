# (1) max(list) 找最大 | min(list) 找最小
# list: item 一定都要是數字
items = input().split()  # items 是串列 ['20', '48', '30']

my_list = []
for i in range(len(items)):
    my_list.append(int(items[i]))
# print(my_list)
print(max(my_list))


# 串列的操作
# 1. 取用 indexing
# 2. 新增 item    -> .append()
# 3. 刪除 item    -> .pop()
# 4. 數 item 有重複幾個 -> .count(item)
# 5. 排順序 -> .sort()
# 6. 翻轉   -> .reverse()

# (2) 
# 20 48 30
# split() 將 str 分成多個 str 構成的串列
items = input().split()  # items 是串列 ['20', '48', '30']

my_list = []
for i in range(len(items)):
    my_list.append(int(items[i]))
# print(my_list)
my_list.sort()  # 排好的串列
print(my_list[-1])