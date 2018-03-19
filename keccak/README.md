Python binding for SHAKE128
===========================

`CompactFIPS202.py` is a
[file](https://github.com/gvanas/KeccakCodePackage/blob/master/Standalone/CompactFIPS202/Python/CompactFIPS202.py)
from the official
[KeccakCodePackage](https://github.com/gvanas/KeccakCodePackage).

`keccak.c` originates from
[Keccak-more-compact.c](https://github.com/gvanas/KeccakCodePackage/blob/master/Standalone/CompactFIPS202/C/Keccak-more-compact.c),
again from the official
[KeccakCodePackage](https://github.com/gvanas/KeccakCodePackage). We
simply added a `FIPS202_SHAKE128_ITER` function to avoid using loops in
Python.

`keccak.py` contains the
[ctypes](https://docs.python.org/3/library/ctypes.html) binding.

Performance
-----------

The speedup between the pure Python version and the DLL calls is
approximately x40, as shown by executing `python3 -m keccak.speed_test`.
