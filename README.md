Hash-based signatures
=====================

**Louis Abraham** and **Yassir Akram**

Instructions
------------

Just `make`.

To run the tests: `make test`

We used [pytest](https://docs.pytest.org/en/latest/), but it will
automatically be installed by the `Makefile`.

API
---

`lamport.py` and `winternitz.py` provide 3 simple functions:

``` pycon
>>> from lamport import *
>>> secret, public = key_generation()
>>> msg = getrandom(32)
>>> sign = signature(msg, secret)
>>> verify(msg, sign, public)
True
```

Using `merkle.py` is just as simple:

``` pycon
>>> from merkle import MerkleTree
>>> from utils import getrandom
>>> m = MerkleTree(HEIGHT=7)
100%|██████████████████████████████████████████████████| 128/128 [00:17<00:00,  7.41it/s]
>>> m.public_key
b']"F\xfd;)Ln\x01\x8a\x8d^\xb1\xb7\xdf|\x88\x11\xcc\x90\xf8\xd2U\xc2Lx\xac\xbab\xec\x00W'
>>> msg = getrandom(32)
>>> sign = m.signature(msg)
>>> m.last_key_used
0
>>> m.verify(msg, sign, m.public_key)
True
>>> msg = getrandom(32)
>>> sign = m.signature(msg)
>>> m.last_key_used
1
```

Performance
-----------

Our code generates a Merkle tree with 1024 keys in about two minutes and
a half. The whole test suite (including the generation of the Merkle
tree) executes more than 4000 signature verifications and takes roughly
500 seconds.

Despite having written the OTS and Merkle tree in Python, the code for
`SHAKE-128` is written in C and compiled to a DLL. This allowed a x40
speedup. To know more, see `keccak/README.md`.

Additional features
-------------------

There is a progressbar for the key generation in the MerkleTree class.
