'''
給定一串字 bbb 請整理出這個字母重複出現幾次，以範例格式表示。

輸入範例1    bbb
輸出範例1    3b

輸入範例2    IIII
輸出範例2    4I
'''

# 流程？

'''
先有輸入 input
計算 input 的長度  -> len()
輸出 len + 
n = input()         # input() -> string   |   string indexing  取索引值   [0] [1]   像是 list, tuple, string
length_n = len(n)
s = ''
s += str(length_n) + n[0]
print(s)
'''

































'''
給定一串字 aaaaaaazzzzcccccddkkkkkjjjjjjj 請整理出每個字母重複出現幾次，以範例格式表示。

輸入範例    aaaaaaazzzzcccccddkkkkkjjjjjjj
輸出範例    a7z4c5d2k5j7
輸出解釋    a7 代表 7 個 a | z4 代表 4 個 z...
'''


# 流程
'''
與上面例子中不一樣的地方
1. 不確定每個字重複的次數 -> len()  (X)

 ' aaaaaaazzzzcccccddkkkkkjjjjjjj'
-> a------z---
-> 12345671234
->       v   V

重複 (for c in str)
    判斷式：判斷前後兩個字一不一樣（需要紀錄前一個字）

'''
input_str = ' ' + input() + ' '     # ' aaaaaaazzzzcccccddkkkkkjjjjjjj '

prev = ' '
counter = 0
result = ''     # 'a7z4.....

# ' a'
for c in input_str:
    # c 每次取一個字母
    if c != prev:
        result += prev + str(counter)  # 把 a7、z4 串接到 result
        counter = 1 # 歸零（從 1 開始數）
        prev = c    # 為了接下來的重複做準備    
    else:
        # c == prev
        counter += 1

print(result[2:])