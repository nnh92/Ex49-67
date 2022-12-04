s = open('Ex58/Ex58.inp', 'r').read()

def Thay_The_Chuoi(s,s1):
    s2 = s[-3:]
    if s2 == 'ing':
        s = s[:-3] + s1
    else:
        s = s + s1
    return s

print(Thay_The_Chuoi(s,'ing'))
