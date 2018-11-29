#! /usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2018-11-28 15:34
# @Author  : Lone
# @File    : get_config.py

import configparser
import os

class GetConfig(object):

    testCnt = 0
    monkeyCmd = []
    pkgName = ""
    # rootPath = os.path.dirname(os.getcwd())
    def get_config(self):
        configPath = "./config/config.ini"
        config = configparser.ConfigParser()
        print("configPath: %s" % configPath)
        config.read(configPath)
        # self.cfg["device"] = config.get("Sample", "device")
        # self.cfg["monkeyCmd"] = config.get("Sample", "monkeyCmd")
        self.monkeyCmd.append(config.get("MonkeyCmd", "monkeyCmd4Normal"))
        self.monkeyCmd.append(config.get("MonkeyCmd", "monkeyCmd4Motion"))
        self.monkeyCmd.append(config.get("MonkeyCmd", "monkeyCmd4AppSwitch"))
        self.testCnt = config.get("TestCfg", "loopCnt")
        self.pkgName = config.get("TestCfg", "pkgName")
        return self.monkeyCmd, self.testCnt, self.pkgName

if __name__ == '__main__':
    monkeyCmd, testCnt, pkgName = GetConfig().get_config()
    print(monkeyCmd)
    print(testCnt)
    print(pkgName)