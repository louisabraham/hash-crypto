from random import randrange

from winternitz import key_generation, signature, verify, SIGNATURE_LENGTH
from utils import getrandom


def modify(sign):
    sign = sign[:]
    i = randrange(SIGNATURE_LENGTH)
    b = getrandom(32)
    while b == sign[i]:
        b = getrandom(32)
    sign[i] = b
    return sign


def test():

    secret, public = key_generation()

    msg = getrandom(32)
    sign = signature(msg, secret)

    assert len(sign) == SIGNATURE_LENGTH
    assert verify(msg, sign, public)

    sign = list(sign)
    assert verify(msg, sign, public)

    false_sign = modify(sign)

    assert not verify(msg, false_sign, public)
    assert verify(msg, sign, public)
