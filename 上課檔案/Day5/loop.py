## 複習
# while 語法
'''
while __狀況判斷__:
    重複的區塊

跳出重複後的程式
'''



# for 語法
'''
for 變數 in 迭代的東西:
    重複的區塊

迭代是指：重複代換
迭代的東西：
1. range(5) -> 0, 1, 2, 3, 4   |   range(start, stop, step) : range(1, 9, 2) -> 1, 3, 5, 7 
2. list:  [3,7,8] -> 3, 7, 8
3. str:   "apple" -> 'a', 'p', 'p', 'l', 'e'

for ch in "apple":
    print(ch)
'''



# continue 跳到下一次重複 | break 跳出重複
'''
零到一百之間印出每個數字，但是不要印 3 的倍數。
1. 先寫好印出零到一百所有數字的程式
2. 如果是 3 的倍數，那麼 continue（跳到下一次）

for i in range(101):
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    print(i, end=' ')
'''


# 練習題：
'''
零到一百之間印出每個數字，但是不要印 3 的倍數，也不要印 5 的倍數。

'''

'''
break: 找最近的迴圈跳出    

for i in range(3): # i == 1
    for j in range(1000): #j == 0
        s = input()
        if s == 'apple':
            break
        print(s)
'''



# 練習題：
'''
1. 零到一百之間印出每個數字，但是不要印 3 的倍數
2. 最後還要補充總共印了幾個數字（數數|計數）。
'''

counter = 0   # 拿在手上的計數器
for i in range(101):
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    print(i, end=' ')
    counter += 1  # counter 加一
    if counter >= 30:
        break

print(f'\n{counter}')


# 練習題：
'''
1. 零到一百之間印出每個數字，但是不要印 3 的倍數，也不要印 5 的倍數
2. 最後還要補充總共印了幾個數字（數數|計數）。



3. 這次我們只要印出前 30 個符合條件的數字就好。
counter > 30 -> break
'''

#  Ctrl + /
