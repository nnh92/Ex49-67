def Xoa_Trung_Lap(s):
    khongtrung = ''
    for i in s:
        if i not in khongtrung:
            khongtrung += i
    return khongtrung


s = open('Ex63/Ex63.inp', 'r').read()

print(Xoa_Trung_Lap(s))