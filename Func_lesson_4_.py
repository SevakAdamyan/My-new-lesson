def my_func(num: int):
    new_list = []
    sum = 0
    while num > 0:
        sum1 = num % 10
        sum = sum1 + sum
        num = num // 10
        new_list.append(sum)
    return new_list


def sort_list(ls:list):
    for i in range(len(ls)):
        for j in range(i, len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] == ls[j], ls[i]
    sort_new_list = []

    sort_new_list = new_list 

    return sort_new_list

my_list =[154, 56, 896, 104]
print(sort_list(my_list))


