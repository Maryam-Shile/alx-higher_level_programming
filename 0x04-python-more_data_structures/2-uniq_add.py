#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq = set()
    for num in my_list:
        if num not in uniq:
            sum += num
            uniq.add(num)
    return sum
