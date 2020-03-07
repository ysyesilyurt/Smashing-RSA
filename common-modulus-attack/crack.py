#!/usr/bin/env/python3

import gmpy2


def extendedGcd(a, b):
    if b == 0:
        return a, 1, 0
    d1, x1, y1 = extendedGcd(b, a % b)
    gcd = d1
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def commonModulusAttack(c1, c2, e1, e2, n):
    gcd, x, y = extendedGcd(e1, e2)
    z = gmpy2.invert(c2, n)
    return (pow(c1, x, n) * pow(z, int(-y), n)) % n



def main():
    with open("crackme.csv", "r") as inp:
        tmp, c1 = inp.readline().split(',')
        tmp, c2 = inp.readline().split(',')
        tmp, e1 = inp.readline().split(',')
        tmp, e2 = inp.readline().split(',')
        tmp, n = inp.readline().split(',')
    resAsInt = commonModulusAttack(int(c1, 16), int(c2, 16), int(e1, 16), int(e2, 16), int(n, 16))
    print(bytes.fromhex(hex(resAsInt).lstrip('0x')).decode('utf-8'))


if __name__ == '__main__':
    main()
