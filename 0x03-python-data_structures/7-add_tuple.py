#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup1 = list(tuple_a)
    tup2 = list(tuple_b)
    tup1 += [0] * 2
    tup2 += [0] * 2
    sum1 = tup1[0] + tup2[0]
    sum2 = tup1[1] + tup2[1]
    sum3 = (sum1, sum2)
    return sum3
