#!/usr/bin/env/python3

import math


def findPivot(ptrace):
    freqs = [0] * 16
    for rec in ptrace:
        freqs[int(math.floor(rec))] += 1
    pivot = -1
    seenFirstRec = False
    sumFreq = 0
    for i, freq in reversed(list(enumerate(freqs))):
        if freq != 0:
            sumFreq += freq
            if not seenFirstRec:
                seenFirstRec = True
        else:
            if seenFirstRec:
                pivot = i + 1
                break

    if sumFreq % 25 != 0 or pivot == -1:
        for j, reFrag in list(enumerate(freqs, start=pivot)):
            sumFreq -= reFrag
            if sumFreq % 25 == 0:
                pivot = j
                break
    return pivot


def findKey(ptrace):
    """
        * Finds decryption key (d) by checking the ptrace.
        * Simply exploits the "exponentiation by squaring" (or square and multiply) implementation of decryption process
        * If a only a square operation is done (during iteration over the bits of d)
               then corresponding bit is 0
               o/w (both square ana multiply operation) then the corresponding bit is 1 in d
    :param ptrace: ptrace of decryption process as lst
    :return: d
    """
    key = []  # exponent
    allHigherConsumptions = []
    tmpCnt = 0
    startCount = False
    pivot = findPivot(ptrace)
    if pivot != -1:
        for rec in ptrace:
            if rec >= pivot:
                if not startCount:
                    startCount = True
                tmpCnt += 1
            else:
                if startCount:
                    if tmpCnt == 125 or tmpCnt == 75:
                        allHigherConsumptions.append(tmpCnt)
                    tmpCnt = 0
                    startCount = False

        for cnt in allHigherConsumptions:
            if cnt == 125:
                key.append('1')
            elif cnt == 75:
                key.append('0')
        return ''.join(key)
    else:
        print("INVALID PIVOT DETECTED")
        exit(1)


def powerAnalysisAttack(ptrace, c, n):
    """
        Exploits RSA implementation by conducting a power analysis on decryption process.
            * Given c,n and ptrace of decryption process, this exploit tries to determine the decryption exponent (d)
            by analyzing the power changes during decryption.
            * After capturing d, m is decrypted easily as: m = c^d (mod n)
    :param ptrace: ptrace of decryption process as lst
    :param c: cipher text
    :param n: modulus
    :return: m (decrypted message)
    """
    d = int(findKey(ptrace), 2)
    m = pow(c, d, n)
    return m


def main():
    """
        Provide a "ptrace.trc" file that contains ptrace of decryption process
        Also provide c and n (one by one) from stdin
        m will be printed to stdout
    """
    with open("ptrace.trc", "r") as inp:
        ptraceLst = list(map(float, inp.readlines()))
    c = int(input(), 16)
    n = int(input(), 16)
    msgAsInt = powerAnalysisAttack(ptraceLst, c, n)
    print(bytes.fromhex(hex(msgAsInt).lstrip('0x')).decode('utf-8'))


if __name__ == '__main__':
    main()
