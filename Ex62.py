def Xoa_Khoang_Trang(s):
    s = s.split()
    return ' '.join(s)

s = open('Ex62/Ex62.inp', 'r').read()

print(s)
print(Xoa_Khoang_Trang(s))