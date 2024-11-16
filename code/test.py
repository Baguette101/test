import pytest

def main():
    test()

def test():
    assert str("hello, World!") == "hello, World!"
    assert 1 == 1

main()