#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from collections import defaultdict


class Singleton(type):
    _instances = defaultdict(dict)

    def __call__(cls, *args, **kwargs):
        name = args[0]
        if cls not in (saved := type(cls)._instances) or name not in saved[cls]:
            saved[cls][name] = super().__call__(*args, **kwargs)
        return saved[cls][name]


class Logger(metaclass=Singleton):
    def __init__(self, name: str = "console"):
        self.name = name
        print(f"Initializing logger {name!r}")


if __name__ == "__main__":
    c1 = Logger("console")
    c2 = Logger("console")
    assert c1 is c2
    s1 = Logger("stream")
    s2 = Logger("stream")
    assert s1 is s2
