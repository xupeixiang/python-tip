#!/usr/bin/python
#!-*- coding: utf-8 -*-
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4

# 给你两个正整数a(0 < a < 100000)和n(0 <= n <=100000000000)，计算(a^n) % 20132013并输出结果

import random

def main():
    for i in range(10):
        a = random.randint(1, 100000)
        n = random.randint(1, 10000000)
        print '%d^%d %% 20132013 = %s' % (a, n, thirtythree(a, n))

def thirtythree(a, n):
    b = a % 20132013    # a ^ n % c = (xc + b) ^ n % c = b ^ n % c   (b < a)
    group_num = int(pow(n, 0.5))  # equally group, making n to 2 * pow(n, 0.5)
    left = n - group_num ** 2

    last = 1
    for i in xrange(group_num):
        last = (last * b) % 20132013
        if last == 0:
            break

    if last != 0:
        new_last = 1
        for i in xrange(group_num):
            new_last = (new_last * last) % 20132013
            if new_last == 0:
                break
        return (new_last * (b ** left)) % 20132013
    else:
        return 0

if __name__ == '__main__':
    main()

