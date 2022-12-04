def Thay_The_Chuoi2(s):
    KQ = ''
    for i in range(len(s)):
        if i%2 == 0:
            KQ = KQ + s[i]
    return KQ

s = open('Ex59/Ex59.inp', 'r').read()

print(Thay_The_Chuoi2(s))