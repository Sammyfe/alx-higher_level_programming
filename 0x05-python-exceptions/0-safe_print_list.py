#!/usr/bin/python3
def safe_print_list(my_list=[], a=0):
    smcl = 0
    for index in range(x):
        try:
            print(my_list[index], end='')
            smcl += 1
        except Exception as error:
            break
    print('')
    return smcl
