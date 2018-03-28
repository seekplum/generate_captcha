#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: generate_captcha
#     FileName: setup
#         Desc: 安装脚本
#       Author: hjd
#     HomePage: seekplum.github.io
#   LastChange: 2018-03-28 13:05
#=============================================================================
"""
import io
import re

from setuptools import setup, find_packages

with io.open('generate_captcha/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name="generate_captcha",
    version=version,
    url="https://github.com/seekplum/generate_captcha",
    keywords="Pil, Captcha, Image",
    description="Generate verification code based on Pil library.",
    long_description=readme,
    license="GPL-3.0",

    author="seekplum",
    author_email="1131909224m@sina.cn",

    packages=find_packages(),
    platforms="any",

    install_requires=[
        "Pillow>=2.8.1"
    ],
)
