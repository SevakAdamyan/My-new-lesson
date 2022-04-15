#Inport any 10 number with keybord, which big to 2 and count how many simpl numbers


from random import randint

my_list = [randint(2, 20) for i in range(10)]
print(my_list)
for i in my_list:
    for j in (i, len(my_list)):
        if i % j == 0 and j % 1 == 0:
            if my_list.count(j) == 2:
               print("It is semple number")


