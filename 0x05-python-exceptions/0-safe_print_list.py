#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new = ''.join(str(i) for i in my_list[:x])
        count = 0
        for n in new:
            count += 1
        print(new)
        return(count)
    except IndexError:
        pass
