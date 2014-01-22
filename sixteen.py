#!/usr/bin/python
#!-*- coding: utf-8 -*-
# -*- indent-tabs-mode: nil; tab-width: 4 -*-
# vi: et ts=4 sts=4 sw=4

# 银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
# 在中文大写方式中，0到10以及100、1000、10000被依次表示为：
#    零壹贰叁肆伍陆柒捌玖拾佰仟万
# 以下的例子示范了阿拉伯数字到人民币大写的转换规则：
#
#    1              圆
#    11             拾壹圆
#    111            壹佰壹拾壹圆
#    101            壹佰零壹圆
#    -10000         负壹仟圆
#    1234567        壹佰贰拾叁万肆仟伍佰陆拾柒圆
#
#    现在给你一个整数a(|a|<100000000), 打印出人民币大写表示

import random

a2z = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','佰','仟','万']

def main():
    for i in range(10):
        a = random.randint(-99999999,99999999)
        print str(a) + ' --> ' + transfer(a)

def transfer(a):
    result = ''
    if a < 0:
        result += '负'
        a = -a
    if a >= 10000:
        result += qian(a / 10000, False) + a2z[-1] + (qian(a % 10000, True) if a % 10000 > 0 else '')
    else:
        result += qian(a, False)
    result += '圆'
    return result.decode("UTF-8")


def qian(a, prefix):
    if a < 1000:
        return bai(a, prefix, prefix)
    else:
        d, m = divmod(a, 1000)
        return a2z[d] + a2z[-2] + (bai(m, False, True) if m > 0 else '')

def bai(a, need_zero, prefix):
    if a < 100:
        return shi(a, True if prefix else False, False)
    else:
        d, m = divmod(a, 100)
        return (a2z[0] if need_zero else '') + a2z[d] + a2z[-3] + (shi(m, False, True) if m > 0 else '')

def shi(a, need_zero, need_shi):
    if a < 10:
        return ge(a, True)
    else:
        d, m = divmod(a, 10)
        return (a2z[0] if need_zero else '') + ('' if d == 1 and not need_shi else a2z[d]) + a2z[-4] + ge(m, False)

def ge(a, need_zero):
    return (a2z[0] if need_zero else '') + (a2z[a] if a > 0 else '')

if __name__ == '__main__':
    main()

