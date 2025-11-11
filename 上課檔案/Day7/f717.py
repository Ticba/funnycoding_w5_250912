x = input().split()   # input(): list ["1", "2", "3", "4", "5"]
x = list(map(int, x))       # list[1, 2, 3, 4, 5]

total = sum(x)

a = total % len(x)  # 5
if a == 0:
    b = len(x)
else:
    b = a

print(b)