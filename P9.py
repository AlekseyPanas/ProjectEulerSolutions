import math

flag = False

for a in range(1, 1001):
    for b in range(a + 1, 1001):
        c = (a ** 2 + b ** 2) ** (1/2)
        if a + b + c == 1000:
            print(a*b*c)
            flag = True
        if flag:
            break
    if flag:
        break
