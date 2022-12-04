def TinhFibonaci(n): 
    if n == 2 or n ==1:
        return 1
    return TinhFibonaci(n-1) + TinhFibonaci(n-2)

try:
    n = int(input('Nhap so fibonaci thu n can tinh: '))
    if n <= 0:
        print('Nhap so nguyen duong!')
    else:
        print(TinhFibonaci(n))

except:
    print('Dinh dang dau vao khong hop le!')