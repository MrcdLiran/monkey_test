#! /usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2018-11-29 10:30
# @Author  : Lone
# @File    : run_test.py

from script4monkey.get_config import GetConfig
from script4monkey.run_monkey import RunMonkey
import time

def run():

    monkeyCmd, testCnt, pkgName = GetConfig().get_config()
    runMonkey = RunMonkey(pkgName)
    runMonkey.connectDevice()
    time.sleep(2)
    runMonkey.appInstall()
    time.sleep(15)

    for i in range(int(testCnt)):
        testCmd = monkeyCmd[i%3]
        runMonkey.runMonkey(testCmd)
        time.sleep(1920)

    time.sleep(10)
    runMonkey.createBugReport()
    time.sleep(10)
    runMonkey.rebootDevice()

if __name__ == '__main__':
    run()