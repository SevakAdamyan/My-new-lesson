#Find the typed number's product and amount.


num = '698'

total = 0
count = 1

for i in num:
    total = total + int(i)
    count = count * int(i)

print("Sum:", total)
print("Product:", count)

