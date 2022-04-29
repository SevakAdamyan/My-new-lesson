def my_func(st:str):
    new_list = []
    for i in range(len(st)):
        for j in range(i, len(st)):
            if chr(i) > chr(j):
               chr(i), chr(j)== chr(j), chr(i)

    new_list.append(st)
    return new_list
st = 'fDgHlOp'
print(my_func(st))