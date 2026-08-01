#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in (saved := type(cls)._instances):
            saved.setdefault(cls, {})
        if (name := args[0]) not in saved[cls]:
            saved[cls][name] = super().__call__(*args, **kwargs)
        return saved[cls][name]


class Logger(metaclass=Singleton):
    def __init__(self, name: str = "console"):
        self.name = name
        print(f"Initializing logger {name!r}")


class Test:
    """
    >>> c1 = Logger("console")
    Initializing logger 'console'
    >>> c2 = Logger("console")
    >>> c1 is c2
    True
    >>> s1 = Logger("stream")
    Initializing logger 'stream'
    >>> s2 = Logger("stream")
    >>> s1 is s2
    True
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
