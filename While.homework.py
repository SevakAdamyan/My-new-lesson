#Write programme, which with keybord can input two numbers and will aggregate, will extract, will deal and will multiply
#numbers. This programme couldn't stop and will say new numbers.Programme will stop,when you input "0".You must tell,
# that you cann't to deal "0" and if you input "0", programme must tell wrong number.



while True:
    num = int(input("any number: "))
    num1 = int(input("any number: "))
    num2 = input("any symbol: ")

    if num2 != 0 and num2 == "/":
       print(num / num1)
    elif num2 == "+":
        print(num + num1)
    elif num2 == "-":
        print(num - num1)
    elif num2 == "*":
        print(num * num1)
    elif num1 == 0:
        break
    else:

        print('new number')