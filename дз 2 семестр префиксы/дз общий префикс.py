def z_func(s, n):
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z



strlst = list(input().split())
stroka = ''.join(strlst)
zlst = z_func(stroka,len(str(stroka)))
slzlst = []
sravlst = []
lnstr = 0

for slovo in strlst:
    lnstr +=len(slovo)
    slzlst.append(lnstr)
slzlst.pop()
for i in slzlst:
    sravlst.append(zlst[i])
indsrezotv = min(sravlst)
print(stroka[:indsrezotv])
    