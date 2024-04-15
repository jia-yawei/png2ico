# **使用tkinter和使用pyqt开发的png转ico小工具**

---

## 两种工具对比

| 工具     | tkinter                                                 | pyqt                                    |
| -------- | ------------------------------------------------------- | --------------------------------------- |
| ui设计   | [tkinter在线布局助手](https://www.pytk.net/)            | qtdesigner                              |
| 设计架构 | ui.py  control.py   main.py                             | ui.ui  ui.py  control.py   main.py      |
| 编程软件 | vscode                                                  | vscode                                  |
| 软件大小 | 25M                                                     | 52M                                     |
| 优点     | 打包后的软件小一点，编程过程比较简单，可以直接使用ui.py | ui开发样式更多，bug少，可用的功能更齐全 |
| 缺点     | ui开发有点小bug，控件的名字很奇葩                       | 打包后的文体积比较大                    |

## 开发流程

### tkinter

使用布局助手进行ui界面开发，推荐[tkinter在线布局助手](https://www.pytk.net/)，有详细的帮助文档，可以直接生成ui和control文件，在control文件内设置回调函数，pyinstall进行打包，打包指令

` pyinstaller --onefile --windowed --icon=myicon.ico --name=myprogram main.py：`

### pyqt

使用qtdesigner界面开发，生成.ui文件，在代码编辑器内使用：

```python
from PyQt5 import uic

if __name__ = '__main__':
    ui = uic.load(./ui.ui)
```

即可将ui文件转为py文件，之后可以将其删除，然后在control文件内设置回调函数，具体细节见源码，pyinstall进行打包，打包指令 ：

` pyinstaller --onefile --windowed --icon=myicon.ico --name=myprogram main.py`
![统计访问次数](https://profile-counter.glitch.me/{ubrong}/count.svg)