# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import re

from tomltoml import tomltoken


def tomltokenize(input_stream):  # noqa
    """Convert an input stream into a token stream."""
    words = filter(None, re.split(r'( )|(\')|(")|(\n)|(=)|(\#)|(\[)|(\])', input_stream))

    i = 0

    while True:
        word = words[i]

        if word == '\n':
            # TODO(wting|2016-09-16): handle newlines within multi-line strings
            yield tomltoken.Newline()
        elif word == '#':
            string = []
            i += 1
            while i < len(words) and words[i + 1] != '\n':
                string.append(words[i])
                i += 1
            yield tomltoken.Comment(''.join(string))
        elif word == '=':
            yield tomltoken.Assignment()
        elif word == '[':
            yield tomltoken.TableStart()
        elif word == ']':
            yield tomltoken.TableEnd()
        elif word == '\'':
            while i < len(words) and words[i + 1] != '\'':
                string.append(words[i])
                i += 1
            yield tomltoken.String(''.join(string))
        elif word == '"':
            yield tomltoken.DoubleQuote()
        else:
            yield tomltoken.Word(word)

        i += 1
