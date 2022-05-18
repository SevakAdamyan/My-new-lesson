def list_to_set(ls:list):
    my_set = set()
    for i in ls:
        my_set.add(i)
    return my_set

my_list = ["apple", "banana", "cherry","google", "microsoft", "apple"]
print(my_list)
print(list_to_set(my_list))