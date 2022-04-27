def my_func(my_list):

my_list = [15, 203, 45, 563, 106]
print(my_list)
my_list1 = []
my_list2 = []
sum = 0
num = 0

for i in len(my_list):
     if i > 0:
         num1 = i % 10
         sum = sum + num1
         i = i  // 10
         list1.append(sum)
         print(my_list1)
         for i in range(len(my_list1)):
             for j in range(i, len(my_list1)):
                 if my_list[i] > my_list[j]:
                     my_list[i], my_list[j] = my_list[j], my_list[i]
                     my_list2.append(my_list1)
                     print(my_list2)
my_func(my_list)
my_func(my_list1)
my_func(my_list2)

















