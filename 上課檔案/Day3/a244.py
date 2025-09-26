# 先給 N 代表輸入的行數

# input :
# 4  # 行數
# 1 2 3
# 2 2 3
# 3 2 3
# 4 2 3

N = int(input())
for i in range(N):
    a, b, c = input().split()  # 1 2 3    string.split()
    a, b, c = int(a), int(b), int(c)
    if a==1:
        print(b+c)
    
    else:
        print(b//c)