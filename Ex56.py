a, b = map(int,input('Nhap 2 vi tri muon cat:').split())

s = open('Ex56/Ex56.inp','r').read()

try:
    if a>b:
        print('Vui long nhap a <= b')
    elif a >= len(s) or b >= len(s):
        print('a hoac b lon hon do dai chuoi!')
    else:
        print(s[b:a-1:-1])
except:
    print('Dinh dang dau vao khong hop le!')