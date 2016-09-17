# -*- coding: utf-8 -*-
# This file is purposely named tomltoken instead of token to prevent shadowing
# the native Python token module
from __future__ import absolute_import
from __future__ import unicode_literals


class Word(object):

    def __init__(self, value):
        self.value = value


class Comment(Word):

    pass


class Operator(object):

    priority = None
    symbol = '\n'


class Newline(Operator):

    priority = 10
    symbol = '\n'


class SingleQuote(Operator):

    priority = 9
    symbol = '\''


class DoubleQuote(Operator):

    priority = 9
    symbol = '"'


class Assignment(Operator):

    priority = 1
    symbol = '='


# TODO(wting|2016-09-16): support inline tables
# TODO(wting|2016-09-16): support table arrays
# TODO(wting|2016-09-16): support dot tables
class TableStart(Operator):
    pass


class TableEnd(Operator):
    pass
