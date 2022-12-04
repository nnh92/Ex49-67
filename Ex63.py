def Thay_The_Nguyen_Am(s):
    NguyenAm = 'auieoAIUEO'
    KQ = ''
    for i in range(len(s)):
        if s[i] in NguyenAm:
            KQ += '$'
        else:
            KQ += s[i]
    return KQ

s = open('Ex63/Ex63.inp', 'r').read()

print(Thay_The_Nguyen_Am(s))