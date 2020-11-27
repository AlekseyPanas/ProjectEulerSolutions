import time

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

div_list = []

num = 600851475143
largest = -1

count = 2

while count <= num:
    if True not in [count % i == 0 for i in div_list]:
        div_list.append(count)
        if num % count == 0:
            largest = count
            print(largest)
    count += 1