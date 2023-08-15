#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
前言：切勿将本工具和技术用于网络犯罪，三思而后行！
文件描述： 
"""
try:
    from typing import List
    from typer import Typer, Option
    from rich import print
    from lib.banner import BANNER
    from lib.check import args_check
    from lib.core import WAFScan
    from lib.report import save_results
except Exception as e:
    print(f"{e}")
    import sys
    import os
    print("[*] Lack of python dependencies, try automatic installation.")
    os.system("pip3 install -r requirements.txt")
    print("[*] Now you can try restarting the program.")
    sys.exit(3)


app = Typer()


@app.command()
def main(
        target: str = Option(None, "--target", "-t", help="扫描单个目标.", ),
        file: str = Option(None, "--file", "-f", help="扫描单个目标.", ),
):
    print(BANNER)  # 输出Banner图案
    target_list: List[str] = args_check(target, file)    # 参数检测
    waf_results: List[dict] = WAFScan().run(target_list)    # 多线程WAF识别
    if waf_results:
        save_results(waf_results)


if __name__ == "__main__":
    app()
