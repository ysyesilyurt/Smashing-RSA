# Smashing RSA for fun and profit?!
Is it possible to break the RSA public-key cryptosystem which is commonly used in encryption/decryption operations of contemporary mediums of secure communication?

## ... how tho?
There are 2 specific attack implementations here, the first one is one of the simplest attack that can be performed on RSA (and also one of the extremely rare one to happen in the real world) is called as _common modulus attack_. In here RSA gets smashed (i.e. we get the plaintext _M_) by two different ciphertexts (_C_) that is acquired with the same modulus _N_ of the same plaintext. You can get a more detailed explanation about [this](https://medium.com/bugbountywriteup/rsa-attacks-common-modulus-7bdb34f331a5) simple attack from this medium article, enjoy :blush:

The other attack adopts a side channel attack mechanism to smash RSA, namely a _power analysis attack_ is performed by exploiting the _implementation_ of the RSA algorithm (not the algorithm itself but its implementation).
