#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: generate_captcha
#     FileName: example
#         Desc: 示例
#       Author: hjd
#     HomePage: seekplum.github.io
#   LastChange: 2018-03-28 14:27
#=============================================================================
"""

import os

from generate_captcha import gen_captcha_text_image


def main():
    # 当前目录
    curr_path = os.path.dirname(os.path.abspath(__file__))

    # 生成验证码
    text, file_path = gen_captcha_text_image(curr_path)
    print("text: {}".format(text))
    print("file_path: {}".format(file_path))


if __name__ == '__main__':
    main()
