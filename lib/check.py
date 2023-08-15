#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
前言：切勿将本工具和技术用于网络犯罪，三思而后行！
文件描述： 
"""
from typer import Exit


def args_check(target: str, file: str) -> list:
    """参数检查

    :param target: 目标域名
    :param file: 本地文件
    :raises typer.Exit: 没有必要参数 退出
    :raises typer.Exit: 如果文件为null 退出
    :return: list 包含目标域名的列表
    """
    def fuc(s):
        return s.rstrip("\n").replace(" ", "").rstrip("/")

    if not (target or file):
        print('You need to provide the args, enter "--help" for help!')
        raise Exit(code=1)
    # 文件读取目标
    if file:
        with open(file, mode='r', encoding='utf-8') as f:
            tmp: list = f.readlines()
            target_list: list = [fuc(i) for i in tmp if fuc(i)]  # 去掉多余的 \n 空格 /
        if not target_list:
            print('The file is null!')
            raise Exit(code=1)
    else:
        target_list: list = [target.rstrip("/")]
    return target_list
