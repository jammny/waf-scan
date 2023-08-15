#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
前言：切勿将本工具和技术用于网络犯罪，三思而后行！
文件描述： 
"""


def runtime_format(start_time: float, end_time: float) -> str:
    """计算程序运行时长，格式化输出结果

    :param start_time: 程序开始时间
    :param end_time: 程序结束时间
    :return: 程序运行时长
    """
    run_time: float = end_time - start_time
    seconds: int = int(run_time)  # 秒
    # milliseconds = int((run_time - seconds) * 1000)   # 毫秒
    if seconds > 60:
        mintues: int = seconds // 60
        new_seconds: int = seconds % 60
        formatted_time = f"{mintues}min {new_seconds}s"
    else:
        formatted_time = f"{seconds}s"
    return formatted_time