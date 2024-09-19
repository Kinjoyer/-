a = list(map(int, input().split()))
c = a.count(a[1])
chast = a[1]
for i in range(len(a)):
    if a.count(a[i])>c:
        c = a.count(a[i])
        chast = a[i]
print(chast)
    