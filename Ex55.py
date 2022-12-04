def KiemtraChuoi(s1, s2):
    if s2 in s1:
        return s1.count(s2)
    else: 'Chuoi "{}" khong xuat hien trong chuoi "{}"'.format(s2,s1)

f = open('Ex55\Ex55.inp', 'r')
s1 = f.readline()
s2 = f.readline()

print('Chuoi "{}" xuat hien {} trong chuoi "{}" '.format(s2,KiemtraChuoi(s1, s2),s1))