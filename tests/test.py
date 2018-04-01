#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#=============================================================================
#  ProjectName: generate_captcha
#     FileName: test
#         Desc: 测试
#       Author: hjd
#     HomePage: seekplum.github.io
#   LastChange: 2018-03-28 13:31
#=============================================================================
"""
import os
import unittest

from generate_captcha import gen_captcha_text_image


class TestGenerateCaptcha(unittest.TestCase):
    def setUp(self):
        pass

    def test_gen_captcha_text_image(self):
        """测试生成验证码图片
        """
        curr_path = os.path.dirname(os.path.abspath(__file__))
        text, file_path = gen_captcha_text_image(curr_path)

        # 验证码生成成功
        assert os.path.exists(file_path)

        # 文件名和预想一致
        file_name = os.path.basename(file_path)
        file_name = file_name.split(".")[0]
        assert text == file_name

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
