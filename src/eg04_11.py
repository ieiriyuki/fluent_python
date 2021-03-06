#!usr/bin/env python

import locale
import sys


expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open("test", "w")

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), "->", repr(value))
