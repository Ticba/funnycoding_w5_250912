"""
EOF: End of File

解題網站改程式的邏輯（四件事情）
(1) 以 python 執行
(2) 執行 XX.py 檔案
**(3) 以 XX.in 作為輸入，取得 XX.out 輸出
(4) 比對 XX.out 與後台答案 XX.ans 是否一致

終端機模擬：
(1) (2) < (3)
python 上課檔案/Day7/EOF_example.py < 上課檔案/Day7/data.in

輸出存入 XX.out
"""

# 請讀取到 EOF 

# 先跟你說有幾行

# while True:
#     try: # 嘗試看看會不會錯，不會錯就執行
#         print(input())
        
#     except: # 出錯的時候會跳來這個區塊
#         break

n = int(input())

for i in range(n):
    print(input())