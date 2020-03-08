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

    exponent = int(findKey(ptraceLst), 2)
    # m = pow(c, 1/exponent, n)
    return m

def main():
    with open("ptrace.trc", "r") as inp:
        ptraceLst = list(map(float, inp.readlines()))
    c = int("4916db7caa1a0dfd3e9b9c7a2aa2bd68d15fc6771a4a75fc00d47cc40f81612854c3dad7f6b275d3d38925a0d44abb9ebd83db256919cc71a47ac84328f840ff6e3e6797ba05d78c57a0cc79722c0dca8c8ff48b74152040462ff445e44388f57a12585fac97a3ca2675c98154d47bf10976ebf0926e6bc2694b04194b2653308e7577da48497fbd88a0a97b20d09421ff9a0ad8ec7ebc67c9c61fd9cb54ef1e825ac5352b689b0d193e70db1c17af8967d93b71b865b81f8ec6db7a39e4fbb830ec2ed0f1ae8d3ae832e0b3b03904b7b46010669a5beb85352fe6f7c0f442ae01fd1376c9c2062b905da18516a90d780e416fc55235b3bd32595031821cc025b32bdcc01cfa5164047a2ceba7a77057a5464cfeb78ddf5145eb88024fc1932322edb501eb3bcf8d585dbdbe4b443542eea4f923611692e399d3cda77bcbcb8e94ce3c6245aaddfc799b6fe2be6e53ae098b2dfc0439ace971f43820173b8a1c5ef54352f714b53c29f3cf0fd88710e71042d7a89bebe34b0ee8713f47b44a6b3f89bcd85366b27e78a2f70d4b1135a3eecddd09d025176abfd15658b20cc75aa173d7998d3de2184b6d9fa8a8cd2591e98164e52a71698b24069c56eb4e549114f484e3cf5644f15dad5c5beb96fbbe83d6b3239af16b700cfbaa7086fc24f85e4c60d4d66ca6e7cc66f5ed48b9fde8937e0df7d86c68bb3b2a7edacaf157a8", 16)
    n = int("adc2c22676ab14b78b7659f8a75856c79a54dce49523af451723669aa065ae6b32e826a810ae3ee2ff33483da8a8c1af20de575e09106462edeee5e4e92346ffcfd1ee352e07700cc2f6b8c4a2a6cc37c61fcdad0202c8504e7619f66d319e4ececdeffc379e4ac4de6761a2f279e2ba36debff57d56a953a14ef3bd27ee08747f7027b75e4f0e1730a03b566e183e2410b6d107f1fed4ab83cdbb5ef03d382d236dc91b924ad127cab4d482bf6d296f3d21bb1dce1d92f079899d3cc5ccbe2dc4e9b4653058af2d24fb096ecdec40c3ac678a74ac7e0e5c26b26cc7698d051892c00426cf39db9309e016216a3f8eaff275624b4cf160b373f240f9e6f6165cea30be8f496d00f77dd2eef66042c62054c70f25c0bad2c8f775f16fb521656a9803232ad32ed272220d2a5c795baf2c5d6076d09f32d4b56390129ed49904009be0cd4db5f25f269e239389b6ae42d6634bb9dceb4e9ff4c8918a384229fcea65d7f6812026edeb256759ef6c58f78897242105bb255c69b37d5fe80ebe10485bf351b86738409bc5894d6a045f18b07181283892ac724b65ea76daf36b995953657d2142564626104f77e3b25265ee383928dfbd1966f208fb17bd6a7d4619dc4ac5edf1705ecfeb5f5e8faa0a1a4907ff997232820a8079044ca5670b1b0fc4191c9297fb624d7f5c7ea6ec537aedea29265d827d482abb6415aa5ec5f761", 16)
    # c = int(input(), 16)
    # n = int(input(), 16)

    msgAsInt = powerAnalysisAttack(ptraceLst, c, n)
    print(msgAsInt)
    # resAsInt = commonModulusAttack(inps['c1'], inps['c2'], inps['e1'], inps['e2'], inps['n'])
    # print(bytes.fromhex(hex(resAsInt).lstrip('0x')).decode('utf-8'))


if __name__ == '__main__':
    main()
