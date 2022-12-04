def Tim_Chuoi(s):
    s = s.split()
    max = s[0]
    id = 0
    for n in s:
        if len(n) > len(max):
            max = n
    return max

s = open('Ex66/Ex66.inp', 'r').read()

print(Tim_Chuoi(s))