# 安装与Demo

### win10的cmd无法运行python
主要为win10环境变量问题，有2种解决方案：
1. 安装python3.9时勾选自动补全环境变量(environment parameters)
2. 在此电脑-属性-高级高级系统设置-环境变量中添加

### import numpy时出现“sanity check...runtime"
主要为windows和numpy最新版本(1.19.4)的匹配存在问题，有解决方案：
pip uninstall numpy
pip install numpy==1.19.3

### 运行Demo.py出现AttributeError: module 'vrep' has no attribute 'simxFinish'
主要为缺少vrep.py与vrepConst.py，与Demo.py放入同一文件夹即可运行
