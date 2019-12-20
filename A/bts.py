#!/usr/bin/env python
# -*- coding:utf-8 -*-
class product():
    size='6寸'
    yang=all
    def __init__(self,color):
        self.color=color

    def call(self):
        print('hello')
    def send_message(self):
        print('快递来了')

phone1=product('pink')
print(phone1.color)
print(phone1.send_message())