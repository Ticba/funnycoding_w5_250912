'''
數字分類： (1) Integer 整數 (2) floating number 浮點數（小數點）


複製 (Ctrl + C) 貼上 (Ctrl + V)   剪下 (Ctrl + X)  還原 (Ctrl + Z)
複製、剪下、貼上也可以操作一整行

選取 (Shift + 方向鍵)、 多重重複選取 (Ctrl + D)
整行上下移動 (Alt + 上/下)




材料      -> 機器 -> 產品
使用者輸入 -> Python -> 輸出：文字、畫面

print('hello!') # 'ssjkd;lfjaks' -> 人類的語言 (str) String

print(123)      # 123            -> 數字 (int) Integer
print(123 + 456)# 123 + 456 (X)  -> 579

print('hello!')


user input : 數字   -> 機器運作 -> 輸出那個數字
123
123
x = int(input('輸入數字'))
print(x)

user input : 數字   -> 機器運作 -> 輸出那個數字，還要再輸出數字*2 的結果
x = int(input('輸入數字'))
print(x,x*2)




string 操作

s = "123 456"
split() 切割
print(s.split()) # ['123', '456'] -> '123' 在第 0 節車廂, '456' 在第 1 節車廂

train = s.split()
print(train[0])  # train[0] -> train 的第 0 節車廂
'''

# user input : 數字1 數字2   -> 機器運作 -> 輸出 數字2+1 數字1+1
s = input("輸入兩個數字:")
#切割
train = s.split()
# 輸出不同車廂內的資料
print(int(train[1])+1, int(train[0])+1) # train[1] -> str

# user input : 數字1 數字2 數字3 -> output: 數字1 + 數字2 + 數字3
# 15 30 45 -> 90