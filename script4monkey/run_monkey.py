#! /usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2018-11-28 15:22
# @Author  : Lone
# @File    : run.py

import time, os
from script4monkey.get_config import GetConfig

class RunMonkey(object):
    def __init__(self, pkgName):
        self.rootPath = os.getcwd()
        self.pkgName = pkgName

    def connectDevice(self):
        conCmt = "adb devices"
        os.popen(conCmt)
        print("Devices has been connected")
        time.sleep(2)

    def appInstall(self):
        print("Ready to start installing apk...")
        apkPath = "./apk"
        apkName = [f for f in os.listdir(apkPath)][0]
        apkPathAbs = self.rootPath + "/apk"
        print(apkPathAbs)
        print(apkName)
        installCmd = r"adb install -r %s/%s" % (apkPathAbs, apkName)
        print(installCmd)
        os.popen(installCmd)
        print("install apk done!")
        time.sleep(15)

    def killTestApp(self):
        killCmd = "adb shell am force-stop %s" % self.pkgName
        os.popen(killCmd)

    def runMonkey(self, monkeyCmd):
        self.killTestApp()
        time.sleep(2)
        print("Running monkey....")
        print("Cmd: %s" % monkeyCmd)
        os.popen(monkeyCmd)
        time.sleep(1920)

    def createBugReport(self):
        print("create bugreport file...")
        bugReportCmd = r"adb shell bugreport > %s/bugreport.txt" % self.rootPath
        print(bugReportCmd)
        os.popen(bugReportCmd)

        time.sleep(180)
        print("create bugreport file ,done")
        chkbugreport = r"java -jar %s/chkbugreport.jar %s/bugreport.txt" % (self.rootPath, self.rootPath)
        print(chkbugreport)
        os.popen(chkbugreport)
        time.sleep(10)

    def rebootDevice(self):
        rebootCmd = "adb reboot"
        os.popen(rebootCmd)



# if __name__ == '__main__':
#     config = GetConfig().get_config()
#     print(config["monkeyCmd"])
#     runMonkey = RunMonkey(config["monkeyCmd"])
#     runMonkey.connectDevice()
#     time.sleep(2)
#     runMonkey.appInstall()
#     time.sleep(15)
#     runMonkey.runMonkey()
#     time.sleep(300)
#     runMonkey.createBugReport()
#     time.sleep(10)