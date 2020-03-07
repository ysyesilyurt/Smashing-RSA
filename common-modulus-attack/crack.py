#!/usr/bin/env/python3

import gmpy2


def extendedGcd(a, b):
    """
    Extended Euclidean Algorithm that also returns x and y where gcd(a,b) = a * x + b * y
    :param a: e1
    :param b: e2
    :return: (gcd, s, t)
    """
    if b == 0:
        return a, 1, 0
    d1, x1, y1 = extendedGcd(b, a % b)
    gcd = d1
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def commonModulusAttack(c1, c2, e1, e2, n):
    """
    Attacks RSA ciphers to find m given c1, c2, e1, e2 and n (the same modulus used for both c1 and c2)
        * First we need to calculate x and y such that gcd(e1,e2) = 1 = e1 * x + e2 * y
            using Extended Euclidean Algorithm
        * Now we have c1^x * c2^y = m (mod N) in our hand; calculating the multiplicative inverse of c2 and N
            (say z), we are going to get m which is given by m = (c1^x) * (z^-y) % N
    :param c1: cipher text 1
    :param c2: cipher text 2
    :param e1: first public encryption exponent used with same modulus
    :param e2: second public encryption exponent used with same modulus
    :param n: modulus
    :return: m (deciphered message)
    """
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
