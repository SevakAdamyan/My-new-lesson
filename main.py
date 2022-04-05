#Input a year from keypboard,identify it as leap or not leap year.


year = int(input("any year"))

if year / 4 == 0 and year / 100 != 0:
    if year / 400 == 0:
        print('leap year')
else:
    print('isnt leap year')


