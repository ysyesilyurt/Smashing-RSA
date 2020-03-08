#!/usr/bin/env/python3

import gmpy2 # TODO: verify

def findKey(ptraceLst):
    key = [] # exponent
    allHigherConsumptions = []
    squareMultDuration = -1 # TODO: check hng
    tmpCnt = 0
    startCount = False
    for rec in ptraceLst:
        if rec > 8: # TODO: verify
            if not startCount:
                startCount = True
            tmpCnt += 1
        else:
            if startCount:
                if squareMultDuration == -1:
                    squareMultDuration = tmpCnt
                elif squareMultDuration < tmpCnt:
                    squareMultDuration = tmpCnt
                allHigherConsumptions.append(tmpCnt)
                tmpCnt = 0
                startCount = False

    for cnt in allHigherConsumptions:
        if cnt == squareMultDuration:
            key.append('1')
        else:
            key.append('0')
    return ''.join(key)


def powerAnalysisAttack(ptraceLst, c, n):
    """

    :param ptraceLst:
    :param c:
    :param n:
    :return:
    """
    d = int(findKey(ptraceLst), 2)
    m = pow(c, d, n)
    return m


def main():
    with open("ptrace.trc", "r") as inp:
        ptraceLst = list(map(float, inp.readlines()))
    c = int(input(), 16)
    n = int(input(), 16)
    msgAsInt = powerAnalysisAttack(ptraceLst, c, n)
    print(bytes.fromhex(hex(msgAsInt).lstrip('0x')).decode('utf-8'))


if __name__ == '__main__':
    main()
