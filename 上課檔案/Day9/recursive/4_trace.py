def f(n):
    print("call", n)
    if n == 0:
        return      # 單純回傳空的，跳出函式
    f( n-1 )
    print("back", n)

f(3)

# 輸出 f(3) 的 call
# 呼叫 f(2)
# 輸出 f(2) 的 call
# 呼叫 f(1)
# 輸出 f(1) 的 call
# 呼叫 f(0)
# 輸出 f(0) 的 call

# f(0) 回傳（任務結束）
# 輸出 f(1) 的 back （任務結束）
# 輸出 f(2) 的 back （任務結束）
# 輸出 f(3) 的 back （任務結束）

# output:
# call 3
# back 2
# back 1
# back 0