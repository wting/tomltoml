# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup

setup(
    name='tomltoml',
    version='0.0.1',
    description='Parser for Tom\'s Obvious Markup Language',
    author='William Ting',
    author_email='io at williamting.com',
    url='https://github.com/wting/tomltoml',
    packages=find_packages(exclude=['tests']),
    setup_requires=['setuptools'],
    install_requires=[],
    license='MIT',
)
