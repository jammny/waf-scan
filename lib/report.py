#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
前言：切勿将本工具和技术用于网络犯罪，三思而后行！
文件描述： 
"""
import random
import string
import json
import time
from os import mkdir
from pathlib import Path

from lib.log import logger


class GetKey:
    def random_key(self, length):
        """
        获取随机
        :param length:
        :return:
        """
        numOfNum = random.randint(1, length - 1)
        numOfLetter = length - numOfNum
        slcNum = [random.choice(string.digits) for i in range(numOfNum)]
        slcLetter = [random.choice(string.ascii_letters) for i in range(numOfLetter)]
        slcChar = slcNum + slcLetter
        random.shuffle(slcChar)
        getPwd = ''.join([i for i in slcChar])
        return getPwd


def save_results(data: list):
    """保存扫描结果

    :param keyword:命名关键字
    :param data: 需要写入的数据
    :return:
    """
    name: str = f"waf_{GetKey().random_key(5)}"
    report_dir = Path("report")
    # 如果目录不存在就创建
    if not report_dir.exists():
        mkdir(report_dir)
    # 写入json
    with open(f'{report_dir}/{name}.json', encoding="utf-8", mode="w") as f:
        json.dump(data, f)
    logger.info(f"Report output：{report_dir}/{name}.json")
