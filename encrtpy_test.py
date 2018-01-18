#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-3 下午5:44
# @Author  : CarryHJR
# @File    : encrtpy_test.py

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import base64


def encrypt(s):  # 加密账号密码
    return '{B}'+ base64.b64encode(s)

print(encrypt('123456'))