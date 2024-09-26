def eratos():
    num = int(input('Введите число: '))
    lst = list()
    a = 2
    b = 1
    while a <= num:
        if num % a == 0:
            if a == 2:
                lst.append(a)
            else:
                while b < a:
                    b += 1
                    if a % b == 0:
                        break
                    elif b == a - 1:
                        lst.append(a)
                        break
                b = 1
              
        a += 1
    return lst
b = eratos()
print(b)   