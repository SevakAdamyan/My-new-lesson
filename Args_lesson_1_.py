# Գրել ֆունկցիա որը կստանա,ոչ բացասական թվերի մատրիցա։ Հաշվեք յուրաքանչյուր սյունակի տարրերի գումարը:
# Ֆունկցիան պետք է վերագարձնի ամենամեծ գումարը և համապատասխան սյունակի հերթական համարը:
# Որոշեք, թե որ սյունակն է պարունակում առավելագույն գումարը:
from random import randint

def matrix(n:int):
    mat = []

    for i in range(n):
        row = [randint(2,100) for i in range(n)]
        mat.append(row)
    return mat
def sum_my_func(num:int):
    my_list = []
    sum = 0
    while num > 0:
        sum=+ sum % 10
        num = num // 10
        my_list.append(num)
    return my_list

def sort_matrix(*args):
    for i in range(len(matrix)):
        if matrix[i] > matrix[i+1]:
            matrix[i],matrix[i+1] == matrix[i+1], matrix[i]
    return matrix
sort_matrix = matrix(10)














