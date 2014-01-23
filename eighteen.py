#!/usr/bin/python
#!-*- coding: utf-8 -*-
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4

#我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
#今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
#输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。

import random

def main():
    for i in range(10):
        a = random.randint(1, 10)
        b = random.randint(a, 40)
        print '(%d, %d) --> (%s)' % (a, b, eighteen(a, b))

def eighteen(a, b):
    prd = a * b
    solutions = []
    min_a_b, max_a_b = min(a, b), max(a, b)
    for num in range(min_a_b, max_a_b + 1):
        d, m = divmod(prd, num)
        if num > d : break
        if m != 0 or num % min_a_b != 0 or d % min_a_b != 0: continue
        ok = True
        for div in range(min_a_b + 1, num + 1):
            if div != 1 and num % div == 0 and d % div == 0:
                ok = False
                break
        if ok : solutions.append((num, d))
    if solutions:
        return ' '.join(map(str, min(solutions, key = lambda a: a[0] + a[1])))
    else:
        return 'N/A'

if __name__ == '__main__':
    main()

