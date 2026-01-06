# 輸入：I'm a master.
# You are my servant.

# 工具 string.isalpha(), string.upper()
# string.isalpha() -> 回傳 True(是字母)、False(不是字母)
# string.upper()   -> 將字轉成大寫

servants = {
    'A':'Saber',
    'B':'Lancer',
    'C':'Archer',
    'D':'Rider',
    'E':'Caster',
    'F':'Assassin',
    'G':'Berserker',
}

c = 'h'

c = c.upper()
diff = ord(c) - ord('A')
# print(ord(c))

餘數 = diff % 7
# print(餘數)

對應的ASCII = ord('A') + 餘數
# print(chr(對應的ASCII))

# H(7) -> A(0)    |  7%7 == 0
