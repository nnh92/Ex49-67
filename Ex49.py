def GiaiThua(n):
    if n:
        return n*GiaiThua(n-1)
    return 1

n = int(input('Nhap so tu nhien n = '))

print(GiaiThua(n))