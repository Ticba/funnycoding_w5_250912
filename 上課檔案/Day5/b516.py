n = int(input())  # n 存總共有幾行

for i in range(n):
    x = input() # x 某一行字
    # len() => str, list, tuple 長度
    x_len = len(x)
    
    for j in x:
        print(j)
        # 每個字母轉換的邏輯
        

    # y = ord(x)
    # y += 3
    # if y > ord('Z'):
    #     y = y-26
    # a = chr(y)
    # print(a)

# input: 'A'
# output: 65