# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from tomltoml.lexer import tokenize
from tomltoml.lib.data_structures import Queue
from tomltoml.lib.data_structures import Stack
from tomltoml import tomltoken


def create_ast(tokens):
    operators = Stack()
    expression = Stack()

    while tokens:
        token = tokens.pop()
        if isinstance(token, tomltoken.Newline):
            pass
        elif isinstance(token, tomltoken.Operator):
            operators.push(token)
        elif isinstance(token, tomltoken.Word):
            expression.push(token)
        else:
            assert False, "Unrecognized token."

    return expression.pop()


def create_dict(tokens):
    pass


def parse_toml(input_stream):
    tokens = Queue(tokenize(input_stream))
    ast = create_ast(tokens)
    return create_dict(ast)
