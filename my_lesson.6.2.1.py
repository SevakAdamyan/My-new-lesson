#print any list and with keybord input another list.Show in the third list the other lists sum.


my_list = list(map(int, input().split()))
my_list1 = [15, 21, 34, 67, 18]
sum = 0

for i in my_list:
    for j in my_list1:
        if type(j) == int:
            if type(i) == int:
                sum = i+j

    print(sum)