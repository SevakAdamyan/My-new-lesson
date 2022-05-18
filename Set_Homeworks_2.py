def creat_set(ls:list):

    my_set = set()


    for i in ls:
        if ls.count(i) == int(i):
            str(i) * int(i)

        my_set.add(str(i))

    return  my_set

my_list1 = [1, 5, 5,8, 9, 3, 1,  8, 5]
print(my_list1)
print(creat_set(my_list1))








