#Show a message about it, show the remainder after division (if any) ,
#and the whole number after division (anyway).

num1=int(input("number1"))
num2=int(input("number2"))
c=num1/num2
d=num1%num2
if num1%num2==0:
    print(c)
else:
    print(d)
