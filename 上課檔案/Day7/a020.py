dict = {
    # key: value
    "A": 10,
    "J": 18,
    "S": 26,
    "B": 11,
    "K": 19,
    "T": 27,
    "C": 12,
    "L": 20,
    "U": 28,
    "D": 13,
    "M": 21,
    "V": 29,
    "E": 14,
    "N": 22,
    "W": 32,
    "F": 15,
    "O": 35,
    "X": 30,
    "G": 16,
    "P": 23,
    "Y": 31,
    "H": 17,
    "Q": 24,
    "Z": 33,
    "I": 34,
    "R": 25
}

'''
  (2) 英文轉成的數字, 個位數乘９再加上十位數的數字

  (3) 各數字從右邊第二個數字到左依次乘１、２、３、４．．．．8

  (4) 求出(2),(3) 及最後一碼的和

  (5) (4)除10 若整除，則為 real，否則為 fake
'''

# id = input()  # 10 長度的字串，其中第一個是英文字母，其餘是數字
# num = dict[id[0]]
# # 個位數*9 + 十位數
# tens = num // 10
# ones = num % 10

# id_int = list(map(int, id[1:]))

# summation = 0

# summation = tens + ones*9 + id_int[-1]

# for i in range(1, 9): # id_int[0]*8 + 1*7 + 2*6 + 6*5 + 6*4 + 3*3 + 8*2 + 3*1
#     summation += id_int[i-1] * (9-i)

# # print(summation)

# if summation % 10 == 0:
#     print('real')
# else:
#     print('fake')

def is_id_real(id):
    num = dict[id[0]]
    # 個位數*9 + 十位數
    tens = num // 10
    ones = num % 10

    id_int = list(map(int, id[1:]))

    summation = 0

    summation = tens + ones*9 + id_int[-1]

    for i in range(1, 9): # id_int[0]*8 + 1*7 + 2*6 + 6*5 + 6*4 + 3*3 + 8*2 + 3*1
        summation += id_int[i-1] * (9-i)

    # print(summation)

    if summation % 10 == 0:
        return 'real'
    else:
        return 'fake'


id = input()
result = is_id_real(id)
print(result)