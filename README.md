# LOL云顶之弈自动化脚本

版本|日期|作者
--|---|--
1.0|2020.2.18|星空

## 说明

适用于S3赛季云顶之弈

## 使用方法

运行前首先要保证pic文件夹和zoe.exe在同一个路径中

`以管理员权限`运行zoe.exe，打印出脚本成功运行这句话说明脚本运行成功
点开下图所示的云顶客户端界面，脚本会自动进行点击操作。

![](assets/client_ui.png)

ps: 脚本有时会出现误点击的情况，所以建议在LOL客户端和桌面背景之间不要在加入其它程序的窗口。


## 脚本编译

``` shell
pip install numpy
pip install opencv-python
pip install pyinstaller
```

最后在zoe目录中执行下面的语句
``` shell
pyinstaller -F zoe.py
```
