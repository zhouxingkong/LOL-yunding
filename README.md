# LOL云顶之弈自动化脚本

版本|日期|作者
--|---|--
1.0|2020.2.18|星空

## 说明

适用于S3赛季云顶之弈

## 使用方法

推荐参数:
+ LOL客户端分辨率:1280x720
+ 屏幕分辨率:1920x1080

运行前首先要保证pic文件夹和zoe.exe在同一个路径中

`以管理员权限`运行zoe.exe，打印出脚本成功运行这句话说明脚本运行成功
点开下图所示的云顶客户端界面，脚本会自动进行点击操作。

![](assets/client_ui.png)

ps: 脚本有时会出现误点击的情况，所以建议在LOL客户端和桌面背景之间不要在加入其它程序的窗口。

## 扩展

此脚本支持用户自行功能扩展，在pic目录中有如下的文件夹

文件夹|功能
--|--
leftClick|左键实时点击的图标
rightClick|右键实时点击的图标
leftClickDelay|左键延迟点击的图标
dragStart|目前没用
dragEnd|目前没用

带对应路径放入.jpg或.png格式的图片即可完成对该图片的自动匹配点击。

## 脚本编译

在github上下载源码包
``` shell
git clone https://github.com/zhouxingkong/LOL-yunding.git
```

使用pip安装依赖的库文件
``` shell
pip install numpy
pip install opencv-python
pip install pyinstaller
```

最后在zoe目录中执行下面的语句将程序打包成exe文件
``` shell
pyinstaller -F zoe.py
```
