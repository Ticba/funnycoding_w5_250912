'''
輸入：
7 4 40
1 2 4 8  代表 4 個評審給的分數，取中間的平均檢查有沒有大於 40
8 5 2 3
3 4 1 8
7 6 1 5
1 8 4 7
3 2 8 6
1 3 2 7

輸出：
A is for apple.
'''

input_str = input().split()  # 7 4 40
times = int(input_str[0])  # 幾次
people = int(input_str[1]) # 幾個評審
pass_score = int(input_str[2]) # 及格標準

passed_list = []
for i in range(times): # i = 0~6 
    # 檢查
    scores = list(map(int, input().split()))
    n = sum(scores) - max(scores) - min(scores)
    average = n/(people-2)

    # 如果發現及格 -> 要記錄下來 i  passed_list.append(i+1)
    if average >= pass_score:
        passed_list.append(i)

for item in passed_list:
    print(item)  # 清單裡的編號都印出來
if len(passed_list) == 0:
    print('A is for apple.')


# print("\n".join(passed_list))
'''
9 7 10
9 15 13 2 6 3 12
12 14 4 5 3 7 19
10 8 4 14 6 18 19
11 17 1 19 4 6 3
8 13 14 16 12 3 17
4 9 8 3 19 17 7
19 2 12 4 1 15 8
11 16 4 12 1 5 19
1 11 9 6 4 19 15
'''
