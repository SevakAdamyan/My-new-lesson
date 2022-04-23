from random import randint
my_list = [randint(1000, 9999) for i in range(10)]
print(my_list)
new_list = []
sum = 0
i = 0

while i > 0:
       num = i % 10
       sum = num + sum
       i = i //10
print(new_list.append(sum))
print(max(new_list))


