#!/usr/bin/python
#!-*- coding: utf-8 -*-
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4

# 下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
# 棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.bit_length如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1.
# 如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。

import random

def main():
    for i in range(10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        print '(%d, %d) --> (%s)' % (a, b, twentyfour(a, b))

def twentyfour(n, m):
    N, M = n, m
    VISITED = {}
    ACTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    def check(n, m, count):
        if n == 0 and m == 0:
            return count
        elif n < 0 or m < 0:
            return -1
        else:
            steps = []
            VISITED[(n, m)] = count
            for delta_n, delta_m in ACTIONS:
                new_n = n + delta_n
                new_m = m + delta_m
                # pruning
                if new_n < 0 or new_n > N or new_m < 0 or new_m > M  or ((new_n, new_m) in VISITED and count + 1 >= VISITED[(new_n, new_m)]):
                    continue
                else:
                    result = check(new_n, new_m, count + 1)
                    if result > 0 :steps.append(result)
            return min(steps) if steps else -1

    return check(N, M, 0)

if __name__ == '__main__':
    main()

