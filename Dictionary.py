#!/usr/bin/env python

#
# Basic hack
#
# What?Needed??
#       Bison like parser for js
# _WHY? Because I forget things easily

class Dict(dict)
    def __init__(self, keyd, *arguments,**context):
        self._context = context

# Elaborate on that
class Elaboration(Dict)
    pass

# To bind them together... I have no idea what the hell I am doing, here
class Dictionary(Elaboration):
    def __init__(self, *args, **kw):
        pass

#
# Read the input(STDIN), and translate it on the output(STDOUT)
#
class py(object):
    class code(dict):
        pass

#
#... Interface !translate
#
class Rune(py.code, dict, Dictionary):
    pass

def translate(outputs, *runes):
    rune = next(runes)
    output.append(
        translate(next(outputs), rune)
    )
# Dictionary: `py; ~ translate: ``glas.cup
