'''
輸入：
1536  # input()
5     # input()
1234 # 1st guess
2345 # 2nd guess
3456 # 3rd guess
2480 # 4th guess
1536 # 5th guess

for __ 五次的迴圈:
    input()


    print('XAXB')

輸出：
2A0B 
0A2B
1A2B
0A0B
4A0B
'''

ans = input()
times = int(input())
for i in range(times):
    guess = input()  # 儲存猜測
    A = B = 0
    # 用 ans & guess 來檢查 XAXB
    # 從 guess 的第一個數字開始
    # 1.檢查數字在不在 ans 之中 -> __ in ___
    # 2.檢查位置是否完全對應   -> guess[j] == ans[j]
    for j in range(4):  # j = 0~3
        if guess[j] in ans:
            if guess[j] == ans[j]:
                # A 就要+1
                A += 1
            else:
                B += 1
    print(f"{A}A{B}B")
