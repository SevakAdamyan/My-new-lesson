# Input any numbers with keybord in -5 from 4.Count how many positive and ngative numbers.

my_list = []
my_list1 = []


for i in range(-4, 0):
    if i <= 0:
        my_list.append(i)
    for j in range(0, 5):
         if j <= 5:
             my_list.append(j)


print(len(my_list))
print(len(my_list1))