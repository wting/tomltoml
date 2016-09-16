# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from tomltoml import api


def test_loads():
    assert api.loads('') == ''
