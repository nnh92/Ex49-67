def SoHoanThien(n):
    i = 1
    lst = []
    a = 0
    while i <= n:
        if n%i == 0:
            lst.append(i)
        i += 1

    for i in range(0,len(lst)):
        a += lst[i]

    if a == 2*n:
        return n
    else: return 0

def SoHoanThien0toN(n):
    lst = []
    for i in range(n):
        if SoHoanThien(i) != 0:
            lst.append(SoHoanThien(i))
    return lst

try:
    n = int(input('Nhap so thu n: '))

    if n <= 0:
        print('Nhap lai so nguyen duong!')
    else:
        print(SoHoanThien0toN(n))

except:
    print('Dinh dang dau vao khong hop le!')