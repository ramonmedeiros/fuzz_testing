
test:
	python -c 'from tests import test_pokeapi_fuzz; [print(func) for func in dir(test_pokeapi_fuzz) if func.startswith("test")]' | xargs -n 1 -I {}  python3 -m pytest -vs tests -k {}
