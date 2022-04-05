#Enter three different numbers on the keyboard. Find the mean (greater than one but less than the other).

a=int(input('number1'))
b=int(input('number2'))
c=int(input('number3'))
if a>b and a<c:
    print('number1')
elif b>c and b<c:
    print('number2')
elif c>b and c<a:
    print('number3')