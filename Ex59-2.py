def Thay_The_Chuoi2(s):
    KQ = []
    for i in list(s):
        if s.index(i)%2 != 0:
            KQ.append(i)
    return ''.join(KQ)

s = open('Ex59/Ex59.inp', 'r').read()

print(Thay_The_Chuoi2(s))