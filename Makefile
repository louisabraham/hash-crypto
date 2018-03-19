all: deps 

test: deps
	pytest

deps: keccak/libkeccak.so .requirements

keccak/libkeccak.so: keccak/keccak.c
	keccak/build.sh
	
.requirements:
	python3 -m pip install -r requirements.txt && touch .requirements

hash-crypto.zip: clean
	zip -r9 hash-crypto.zip *
	
clean:
	rm -rf hash-crypto.zip keccak/libkeccak.so
	rm -rf __pycache__ keccak/__pycache__
