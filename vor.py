import random
n = int(input('Введите количество экспанатов, которые нужно украсть(целое число): '))
k = int(input('Введите максимальный вес, который может унести вор(целое число): '))
m = int(input('Введите количество заходов, которое есть у вора(целое число): '))
print('\n')
spisok_expanate = []
for i in range(5*n):
    spisok_expanate.append([f"Экспонат #{i}", random.randint(1, k + 5), random.randint(1, 100)])

spisok_expanate.sort(key=lambda x: x[2]*(-1))
print('Список всех экспанатов:', spisok_expanate)

spisok_ukrad = []
while n != 0 and m != 0:
    spisok_vzat = []
    ves = k
    for i in range(len(spisok_expanate)):
        if ves <= 0:
            break
        if spisok_expanate[i][1] <= ves and (spisok_expanate[i] not in spisok_ukrad) and (spisok_expanate[i] not in spisok_vzat):
            ves -= spisok_expanate[i][1]
            spisok_vzat.append(spisok_expanate[i])
    for j in range(len(spisok_vzat)):
        spisok_ukrad.append(spisok_vzat[j])
    n -= len(spisok_vzat)
    m -= 1

print('\n')
print('Список украденных экспонатов:', spisok_ukrad)
print('\n')
summa = 0
for i in spisok_ukrad:
    summa += i[2]
print('Общая цена украденного:', summa)







