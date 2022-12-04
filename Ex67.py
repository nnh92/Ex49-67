def Xu_Ly_Chuoi(s):
    s = s.split('.')
    for i in s:
        i = Xoa_Khoang_Trang(i)
        print(i.title())

def Xoa_Khoang_Trang(s):
    s = s.split()
    return ' '.join(s)

s = open('Ex67/Ex67.inp', 'r').read()

#print(Xoa_Khoang_Trang(s))
print(Xu_Ly_Chuoi(s))