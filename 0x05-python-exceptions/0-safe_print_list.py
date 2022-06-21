#!/usr/bin/python3
def safe_print_list(my_list=[], a=0):
    smpf = 0
    for index in range(a):
        try:
            print(my_list[index], end='')
            smpf += 1
        except Exception as error:
            break
    print('')
    return smpf
