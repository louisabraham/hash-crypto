import ctypes
import ctypes.util

import os.path

libkeccak = ctypes.CDLL(os.path.dirname(__file__) + '/libkeccak.so')


def SHAKE128(inputBytes, outLen):
    inLen = len(inputBytes)
    outputBytes = (ctypes.c_ubyte * outLen)()
    outputBytes_p = ctypes.pointer(outputBytes)
    libkeccak.FIPS202_SHAKE128(inputBytes, inLen, outputBytes_p, outLen)
    return bytes(outputBytes)


def SHAKE128_ITER(it, inputBytes, outLen):
    if not it:
        return inputBytes
    inLen = len(inputBytes)
    outputBytes = (ctypes.c_ubyte * outLen)()
    outputBytes_p = ctypes.pointer(outputBytes)
    libkeccak.FIPS202_SHAKE128_ITER(
        it, inputBytes, inLen, outputBytes_p, outLen)
    return bytes(outputBytes)
