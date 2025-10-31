# input: CODEWARS
# output: 67_79_68_69_87_65_82_83

# 1. C -> 67
# 2. 67 放到 my_list
# 3. 重複 1~2 步驟直到所有數字轉換完
# 4. '_'.join(my_list)   my_list 的 item 都要是字串

s = input()

my_list = []
for c in s:
    item = ord(c)   # ord()  將一個字轉成其 ASCII CODE，例：'A' -> 65
    my_list.append(str(item))
print('_'.join(my_list))
