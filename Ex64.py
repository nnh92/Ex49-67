def Noi_Chuoi(s):
    s = s.split()
    return '-'.join(s)

s = open('Ex63/Ex63.inp', 'r').read()

print(Noi_Chuoi(s))