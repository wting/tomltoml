# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from tomltoml.parser import parse_toml


def dumps():
    pass


def loads(input_data):
    return parse_toml(input_data)
