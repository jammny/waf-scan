#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
前言：切勿将本工具和技术用于网络犯罪，三思而后行！
文件描述： 
"""
NAME = 'F5 BIG-IP (F5 BIG-IP)'


def is_waf(self):
    if self.matchContent(r'操作可能存在安全隐患'):
        return True

    return False