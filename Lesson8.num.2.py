#Find all perfect numbers till 10000.


for i in range(1, 10000):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += i
    if sum == i:
        print(f'Perfect numbers are :  {i}')
