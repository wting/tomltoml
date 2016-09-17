# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from tomltoml import api


def test_loads():
    with open('./tests/examples/simple.toml', 'r') as f:
        assert api.loads(f.read()) == ''
