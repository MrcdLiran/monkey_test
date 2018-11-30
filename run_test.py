#! /usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2018-11-29 10:30
# @Author  : Lone
# @File    : run_test.py

from script4monkey.get_config import GetConfig
from script4monkey.run_monkey import RunMonkey

def run():

    monkeyCmd, testCnt, pkgName = GetConfig().get_config()
    runMonkey = RunMonkey(pkgName)
    runMonkey.connectDevice()
    runMonkey.appInstall()

    for i in range(int(testCnt)):
        testCmd = monkeyCmd[i%3]
        runMonkey.runMonkey(testCmd)

    runMonkey.createBugReport()
    runMonkey.rebootDevice()

if __name__ == '__main__':
    run()