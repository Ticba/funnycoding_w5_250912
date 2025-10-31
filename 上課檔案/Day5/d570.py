# str 操作
s = input()
while len(s)!=0:  # s 不見的時候代表什麼是零？ s 的長度，所以搭配 len()
    print(s)
    s = s[0:-1]   # s[最前面:最後面]