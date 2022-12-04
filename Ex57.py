def DanXenChuoi(s1, s2):
    s = ''
    s2 = s2[::-1]
    for i in range(max(len(s1),len(s2))):
        if i < len(s1):
            s += s1[i]
        if i < len(s2):
            s += s2[i]
    return s

s1 = open('Ex57/s1.inp','r').read()
s2 = open('Ex57/s2.inp','r').read()

print(DanXenChuoi(s1, s2))