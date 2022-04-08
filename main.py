# please input any number and user to count how many bayt or kilobayt.


num = int(input("any number"))
num1 = input('You want to count "b to kb" or "kb to b"')


if num1 == "b to kb":
    print(f"{num} baytes = {num/ 1024} kilobytes")


print(f"{num} kilobayts80 = {num*1024} baytes")
