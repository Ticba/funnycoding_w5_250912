def is_leap(year):     # 是否為閏年： 1. 西元年 ， 先除以 4 餘 0 是閏年 ， 但是如果除以 100 餘 0 不是閏年（100, 200, 300, 500) 。 除以 400 餘 0 是閏年。
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in (1,3,5,7,8,10,12):
        return 31
    return 30

def total_days(y, m, d):
    days = 0

    for year in range(1, y):
        days += 366 if is_leap(year) else 365

    for month in range(1, m):
        days += days_in_month(y, month)

    days += d

    return days

while True:
    try:
        y1, m1, d1 = map(int, input().split())
        y2, m2, d2 = map(int, input().split())

        t1 = total_days(y1, m1, d1)
        t2 = total_days(y2, m2, d2)

        print(abs(t2 - t1))
    except:
        break