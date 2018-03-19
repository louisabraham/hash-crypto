from random import randrange
from utils import getrandom

import pytest

from merkle import MerkleTree


def modify_sign1(sign, n_keys):
    key_index, otssign, otspublic, auth = sign
    i = randrange(n_keys)
    while i == key_index:
        i = randrange(n_keys)
    return (i, otssign, otspublic, auth)


def modify_sign4(sign):
    key_index, otssign, otspublic, auth = sign
    auth = list(auth)
    i = randrange(len(auth))
    r = getrandom(32)
    while r == auth[i]:
        r = getrandom(32)
    auth[i] = r
    return (key_index, otssign, otspublic, auth)


def test():
    """
    No need to test otssign or orspublic
    as they are tested by the OTS test
    """

    m = MerkleTree(progressbar=False)

    for _ in range(m.n_keys):

        msg = getrandom(32)
        sign = m.signature(msg)

        assert MerkleTree.verify(msg, sign, m.public_key)

        false_sign = modify_sign1(sign, m.n_keys)
        assert not MerkleTree.verify(msg, false_sign, m.public_key)

        false_sign = modify_sign4(sign)
        assert not MerkleTree.verify(msg, false_sign, m.public_key)

        assert MerkleTree.verify(msg, sign, m.public_key)

    with pytest.raises(AssertionError) as excinfo:
        msg = getrandom(32)
        sign = m.signature(msg)

    assert excinfo.value.args == ('All keys have been used',)
