#Find count this n numbers 1 -0,5 0,25 -0,125 ... Import n with keybord.

import random

my_list = []
sum = 0

for i in range(0, 1):
    num = random.randint(0, 1)
    my_list.append(num)
    if type(i) == float:
        if i > 0 and i < 1:
           sum += i
           print(sum)
