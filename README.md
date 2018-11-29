# Monkey自动化测试
## 一、使用方法 
### 1. 将待测apk放入apk文件夹
### 2. 填写config.ini文件：
#### - 将自己需要使用的Monkey命令写在[MonkeyCmd]下
#### - 将测试的循环次数与待测apk包名写在[MonkeyCmd]下
#### - 具体格式请详见config.ini
##### ps: 每次循环运行1920s, 既循环15次测试进行8小时整
### 3. 执行run_test.py
### 4. 测试结束后，会自动生成bugreport_out文件夹，index.html为生成的测试报告

## 二、测试策略与使用工具
### 1. 策略：
#### - 使用三种不同的Monkey命令做尽可能多的场景覆盖
#### - 以1920s为一个时间单位进行循环测试，规避长时间测试出现不可忽略ANR问题
### 2. 工具：
#### - [<i class="icon-refresh"></i> chkbugreport github地址](https://github.com/sonyxperiadev/ChkBugReport)