a = input()
n = int(a[0])
lst = []
lstrev = []

for i in range(2, len(a), n):
    lst.append(a[i:i + n])
    
for i in lst:
    lstrev.append(i[::-1])

print(''.join(lstrev))
    
