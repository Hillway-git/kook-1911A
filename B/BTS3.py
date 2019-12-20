#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
import os
try:
    os.mkdir('A')
except FileExistsError:
    print('当文件已存在时，无法创建该文件')
else:

finally:
    print('这句话，无论异常是否发生都会执行。')