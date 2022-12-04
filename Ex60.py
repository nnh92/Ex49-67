def Thay_The_Chuoi3(s):
    if s[0].islower():
        return s.lower()
    elif s[0].isupper():
        return s.upper()
    return s

s = open('Ex60/Ex60.inp', 'r').read()

print(Thay_The_Chuoi3(s))