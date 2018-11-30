#! /usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2018-11-28 15:22
# @Author  : Lone
# @File    : run.py

import time, os
from .logger import Logger

logger = Logger("run_test").getlog()

class RunMonkey(object):
    def __init__(self, pkgName):
        self.rootPath = os.getcwd()
        self.pkgName = pkgName

    def connectDevice(self):
        conCmt = "adb devices"
        os.popen(conCmt)
        logger.info("Devices has been connected")
        time.sleep(2)

    def appInstall(self):
        logger.info("Ready to start installing apk...")
        apkPath = "./apk"
        apkName = [f for f in os.listdir(apkPath)][0]
        apkPathAbs = self.rootPath + "/apk"
        logger.info(apkPathAbs)
        logger.info(apkName)
        installCmd = r"adb install -r %s/%s" % (apkPathAbs, apkName)
        logger.info(installCmd)
        os.popen(installCmd)
        logger.info("install apk done!")
        time.sleep(15)

    def killTestApp(self):
        killCmd = "adb shell am force-stop %s" % self.pkgName
        os.popen(killCmd)

    def runMonkey(self, monkeyCmd):
        self.killTestApp()
        time.sleep(2)
        logger.info("Running monkey....")
        logger.info("Cmd: %s" % monkeyCmd)
        os.popen(monkeyCmd)
        time.sleep(1920)

    def createBugReport(self):
        logger.info("create bugreport file...")
        bugReportCmd = r"adb shell bugreport > %s/bugreport.txt" % self.rootPath
        logger.info(bugReportCmd)
        os.popen(bugReportCmd)

        time.sleep(180)
        logger.info("create bugreport file ,done")
        chkbugreport = r"java -jar %s/chkbugreport.jar %s/bugreport.txt" % (self.rootPath, self.rootPath)
        logger.info(chkbugreport)
        os.popen(chkbugreport)
        logger.info("Bugreport checking....")
        time.sleep(10)

    def rebootDevice(self):
        rebootCmd = "adb reboot"
        os.popen(rebootCmd)



# if __name__ == '__main__':
#     config = GetConfig().get_config()
#     logger.info(config["monkeyCmd"])
#     runMonkey = RunMonkey(config["monkeyCmd"])
#     runMonkey.connectDevice()
#     time.sleep(2)
#     runMonkey.appInstall()
#     time.sleep(15)
#     runMonkey.runMonkey()
#     time.sleep(300)
#     runMonkey.createBugReport()
#     time.sleep(10)