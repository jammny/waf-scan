#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
前言：切勿将本工具和技术用于网络犯罪，三思而后行！
文件描述： 
"""
import logging

from rich.logging import RichHandler


LEVEL = "INFO"

# 配置rich处理器
logging.basicConfig(
    level=LEVEL,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(
        rich_tracebacks=True,
        omit_repeated_times=False,
        markup=True
    )]
)

logger = logging.getLogger("rich")  # 定义记录器
