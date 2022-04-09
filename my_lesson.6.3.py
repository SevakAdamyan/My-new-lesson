num =input('any number: ')

even = 0
odd = 0

for i in num:
    if int(i)%2==0:
       even=even+1
    else:
        odd=odd+1

print(f'Even numbers: {even}, Odd numbers: {odd}')