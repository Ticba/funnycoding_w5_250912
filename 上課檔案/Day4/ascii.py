# 電腦中字符的編號，參考 ASCII Table

# 編號 -> 字符
print(chr(65))

print(chr(66))

# 字符 -> 編號
print(ord('C'))




# 凱薩加密 
# ABC   ->   DEF
# Z  ->   C

#  使用者輸入一個字符（大寫英文字）
#  程式輸出凱薩加密的結果

# c_in = input()
# c_ascii = ord(c_in)   # c_in 字符的 ACSII Code 編碼  | A -> 65
# c_ascii += 3          # c_ascii + 3                 | 65+3 -> 68
# c_out = chr(c_ascii)  #                             | 68 -> D
# print(c_out)


# A 當成起點   ，往後數 1 是 B   ，往後數 25 是 Z   ，不能數到 26  -> 26 等同於 0 | 27 等同於 1
# 26%26 == 0 | 27%26 == 1

c_in = input()
c_ascii = ord(c_in)   # c_in 字符的 ACSII Code 編碼  | A -> 65
c_ascii += 3          # c_ascii + 3                 | 65+3 -> 68
diff = (c_ascii - 65)%26   # 0~25
c_out = chr(65+diff)  #                             | 68 -> D
print(c_out)