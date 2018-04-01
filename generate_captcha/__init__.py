#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: generate_captcha
#     FileName: __init__.py
#         Desc:
#       Author: hjd
#     HomePage: seekplum.github.io
#   LastChange: 2018-03-28 13:30
#=============================================================================
"""

__version__ = '0.0.4'

from .generate_captcha import NUMBERS, LOWERCASE_LETTERS, CAPITAL_LETTERS
from .generate_captcha import gen_captcha_text_image
