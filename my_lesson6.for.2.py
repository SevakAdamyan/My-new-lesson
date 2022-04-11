#Print the new list with keybord and count sum and product in list numbers.

my_list = list(map(int, input().split()))

sum = 0

product = 1

for i in my_list:
    sum+=int(i)
    product*=int(i)

print("Sum:", sum)
print("Product:", product)