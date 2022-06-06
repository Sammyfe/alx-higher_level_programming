#!/usr/bin/python3
def add_tuple(tuple_i=(), tuple_j=()):
    len_a = len(tuple_i)
    len_b = len(tuple_j)

    if len_a == 0:
        a1 = 0
        a2 = 0
    elif len_a == 1:
        a1 = tuple_i[0]
        a2 = 0
    else:
        a1 = tuple_i[0]
        a2 = tuple_i[1]

    if len_b == 0:
        b1 = 0
        b2 = 0
    elif len_b == 1:
        b1 = tuple_j[0]
        b2 = 0
    else:
        b1 = tuple_j[0]
        b2 = tuple_j[1]

    new_tuple = (a1 + b1, a2 + b2)

    return (new_tuple) 
