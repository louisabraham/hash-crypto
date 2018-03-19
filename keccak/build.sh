#!/bin/sh
cd "$( dirname "${BASH_SOURCE[0]}" )"
gcc -std=c99 -shared -o ./libkeccak.so -fPIC ./keccak.c