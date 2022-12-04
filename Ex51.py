def TimSoNguyenTo(a, b):
    lst_SNT = []
    for i in range(a, b+1):
        SL = 0
        for j in range(1, i+1):
            if i%j == 0:
                SL += 1
        if SL == 2:
            lst_SNT.append(i)

    return lst_SNT

try:
    a, b = map(int,input('Nhap 2 so a, b: ').split())

    if a <= 0 or b <=0:
        print('Nhap lai a, b la 2 so nguyen duong!')
    elif a > b:
        print('Nhap lai a<=b!')
    else:
        print(TimSoNguyenTo(a, b))
except:
    print('Dinh dang dau vao khong hop le!')