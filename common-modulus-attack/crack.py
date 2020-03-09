#!/usr/bin/env/python3


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


# def multiplicativeInverse(c2, n):
#     """
#     Returns multiplicative modulo inverse of c2 under N, if exists
#     otherwise returns -1
#     """
#     for i in range(n):
#         if (c2 * i) % n == 1:
#             return i
#     return -1


def multiplicativeInverse(A, M):
    """
    Assumes that A and M are co-prime
    Returns multiplicative modulo inverse of A under M
    """
    # Find gcd using Extended Euclid's Algorithm
    gcd, x, y = extended_euclid_gcd(A, M)

    # In case x is negative, we handle it by adding extra M
    # Because we know that multiplicative inverse of A in range M lies
    # in the range [0, M-1]
    if x < 0:
        x += M

    return x


def extended_euclid_gcd(a, b):
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y
    """
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r  # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return [old_r, old_s, old_t]


def commonModulusAttack(c1, c2, e1, e2, n):
    """
    Attacks RSA ciphers to find m, given c1, c2, e1, e2 and n (the same modulus used for both c1 and c2)
    Assumes the gcd of e1 and e2 is equal to 1 (i.e. e1 and e2 is co-prime)
        * First we need to calculate x and y such that gcd(e1,e2) = 1 = e1 * x + e2 * y
            using Extended Euclidean Algorithm
        * Now we have c1^x * c2^y = m (mod N) in our hand, we can find m using m = (c1^x) * (c2^y) % N but
            since in almost all the cases, the value of y will be negative we first need to calculate the
            multiplicative inverse of c2 and N (say z) which then we are going to use as c2^y = z^-y
        * Finally we are going to find m using m = (c1^x) * (z^-y) % N
    :param c1: cipher text 1
    :param c2: cipher text 2
    :param e1: first public encryption exponent used with same modulus
    :param e2: second public encryption exponent used with same modulus
    :param n: modulus
    :return: m (decrypted message)
    """
    gcd, x, y = extendedGcd(e1, e2)
    z = multiplicativeInverse(c2, n)
    return (pow(c1, x, n) * pow(z, int(-y), n)) % n


def main():
    """
        Provide a "crackme.csv" file that contains needed parameters to initiate the attack,
            required params are: c1, c2, e1, e2, n
        m will be printed to stdout
    """
    inps = {'c1': 0, 'c2': 0, 'e1': 0, 'e2': 0, 'n': 0}
    with open("crackme.csv", "r") as inp:
        lines = inp.readlines()
        for i in lines:
            name, val = i.split(',')
            inps[name] = int(val, 16)
    msgAsInt = commonModulusAttack(inps['c1'], inps['c2'], inps['e1'], inps['e2'], inps['n'])
    print(bytes.fromhex(hex(msgAsInt).lstrip('0x')).decode('utf-8'))


if __name__ == '__main__':
    main()
