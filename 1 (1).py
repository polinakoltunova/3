n = int(input("Сдача: "))
m1, s1 = map(int, input("количество и номинал 1: ").split())
m2, s2 = map(int, input("количество и номинал 2: ").split())
m3, s3 = map(int, input("количество и номинал 3: ").split())
m4, s4 = map(int, input("количество и номинал 4: ").split())
res = []
summ = 0
a = [[m1, s1], [m1, s2], [m3, s3], [m4, s4]]
a.sort(key = lambda x: x[1])
a = sorted(a, reverse=True)
for i in range(4):
    num = min(n // a[i][1], a[i][0])
    res += [[a[i][1], num]]
    n -= a[i][1] * num
    if n == 0:
        break
if n > 0:
    print("невозможно дать сдачу")
else:
    print("комбинация монет для сдачи:", res)
                   
    
