#!/usr/bin/env/python3


def extendedGcd(a, b):
    """
    Extended Euclidean Algorithm - gcd(a,b) = a * x + b * y
        that returns x and y as well as the gcd value of the operands
    :param a: first operand
    :param b: second operand
    :return: (gcd(a,b), x, y)
    """
    res = [a, 1, 0]
    tmpRes = [b, 0, 1]
    while tmpRes[0] != 0:
        # Swap temp with res, then update temp with newly calculated div accordingly #
        div = res[0] // tmpRes[0]
        res[0], tmpRes[0] = tmpRes[0], res[0] - (div * tmpRes[0])
        res[1], tmpRes[1] = tmpRes[1], res[1] - (div * tmpRes[1])
        res[2], tmpRes[2] = tmpRes[2], res[2] - (div * tmpRes[2])
    return res


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
    _, x, y = extendedGcd(e1, e2)
    _, z, _ = extendedGcd(c2, n)
    if z < 0:
        z += n
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
