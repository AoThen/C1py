import sys
import time

import win32api  # winAPI模块--以便于操作窗口  #pypiwin32
import win32con
import win32gui
from PyQt6.QtWidgets import QApplication, QMainWindow

from untitled import Ui_Dialog


def login(address='localhost', port=8080, user='admin', password='123'):
    print('Hi C1py')


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def clearText(self):
        print('clearText')

    def query(self):
        print('query')
        self.hwnd = win32gui.GetForegroundWindow()  # 获取最前窗口句柄
        self.hwnd = win32gui.FindWindow(0, 'wdname')  # 根据窗口标题，取得窗口句柄
        # 函数功能：该函数获得一个顶层窗口的句柄，该窗口的类名和窗口名与给定的字符串相匹配。这个函数不查找子窗口。在查找时不区分大小写
        # 参数1 窗口类名
        # 参数2 窗口标题--必须完整；如果该参数为None，则为所有窗口全匹配
        # 返回值：如果函数成功，返回值为窗口句柄；如果函数失败，返回值为0

        # self.hwnd = win32gui.FindWindow("Notepad", None)  # 根据窗口类名，取得窗口句柄

        print('窗口句柄为：', self.hwnd)
        if self.hwnd != 0:
            win32gui.SetForegroundWindow(self.hwnd)  # 窗口显示最前面
            # 参数：窗口句柄
        text = win32gui.GetWindowText(self.hwnd)  # 获取窗口标题
        print('窗口标题为:', text)
        clsname = win32gui.GetClassName(self.hwnd)  # 获取窗口类名
        print('窗口类名:', clsname)
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)  # 获取窗口位置
        # left, top是左上角坐标；right, bottom是右下角坐标
        print('窗口位置', left, top, right, bottom)

        windows = []  # 自定义参数，可以是任何类型
        # win32gui.EnumWindows(self.ss, windows)  #寻找所有顶层窗口的句柄
        # 参数1：回调函数名称，每找到一个句柄就把句柄和windows传给a和b，并执行一次回调函数
        # 参数2：必须有，可以向回调函数传递一些其它参数--传给b，可以是任何类型
        # 枚举屏幕上的所有的顶层窗口，轮流地将这些窗口的句柄传递给回调函数的a参数。EnumWindows会一直进行下去，直到枚举完所有的顶层窗口，或者回调函数返回了FALSE.

        # 打开一个记事本
        self.hwnd1 = win32gui.FindWindow("Notepad", None)
        print("父窗口句柄：", self.hwnd1)
        win32gui.EnumChildWindows(self.hwnd1, self.sss, windows)  # 寻找子窗口句柄
        # 参数1  父窗口句柄,如果此参数为Null，则此函数等效于EnumWindows；每找到一个句柄就把句柄和windows传给a和b，并执行一次回调函数
        # 参数2 回调函数
        # 参数3 自定义参数
        # 枚举所有子窗口，轮流地将这些窗口的句柄传递给回调函数的a参数。函数会一直进行下去，直到枚举完所有的子窗口，或者回调函数返回了FALSE
        # 特别注意：qt只有一个窗体，里面控件的句柄是找不到的--所以这条指令不能用在Qt绘制的窗口上

        # 打开彗星小助手
        self.hwnd = win32gui.FindWindowEx(0, 0, 0, '彗星小助手')  # 查找窗口或子窗口句柄
        # 参数1 父窗口句柄；如果是 0, 则函数以桌面窗口为父窗口;如果是 HWND_MESSAGE, 函数仅查找消息窗口
        # 参数2 子窗口句柄,必须是参数1的直接子窗口；子窗口以Z序排列，查找参数后面的子窗口；如果是 0, 查找从父窗口的第一个子窗口开始
        # 如果参数1和参数2同时是 0, 则函数查找所有的顶层窗口及消息窗口
        # 参数3 类名
        # 参数4  标题；可以是None
        # 返回找到的第一个窗口的句柄
        print('彗星小助手的句柄：', self.hwnd)

        subHandle = win32gui.FindWindowEx(self.hwnd1, 0, "EDIT", None)  # 笔记本类名为EDIT的句柄
        # 编辑框的句柄

        menuHandle = win32gui.GetMenu(self.hwnd1)  # 获取窗口的菜单句柄
        # 参数 窗口句柄
        print('记事本菜单句柄：', menuHandle)

        subMenuHandle = win32gui.GetSubMenu(menuHandle, 0)  # 获得子菜单或下拉菜单句柄
        # 参数1 菜单句柄
        # 参数2 子菜单索引号
        print('子菜单文件句柄：', subMenuHandle)

        menuItemHandle = win32gui.GetMenuItemID(subMenuHandle, 0)  # 获得菜单项中的的标志符ID，注意，分隔符是被编入索引的
        # 参数1 子菜单句柄--文件菜单句柄
        # 参数2 项目索引号
        # 1
        print(menuItemHandle)

        hwnd = self.hwnd1 = win32gui.FindWindow("Notepad", None)
        i = win32gui.IsIconic(hwnd)  # 检查窗口是否最小化
        # 是  返回1，不是返回0
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)  # 不要最小化
        self.hwnd = win32gui.FindWindow(0, '练习')
        win32gui.PostMessage(self.hwnd, win32con.WM_CLOSE, 0, 0)  # 关闭窗口
        # 参数1 窗口句柄
        handle = win32gui.FindWindow("Notepad", None)
        subHandle = win32gui.FindWindowEx(handle, 0, "EDIT", None)
        i = win32api.SendMessage(subHandle, win32con.WM_SETTEXT, 0, '我是文本')  # 向窗口发送文本
        # 原文本全部被替换
        # 参数1 窗口句柄
        # 参数4 发送的文本
        # 等待窗口处理完毕后返回true
        self.hwnd = win32gui.FindWindow("Notepad", None)
        bufSize = win32api.SendMessage(self.hwnd, win32con.WM_GETTEXTLENGTH, 0, 0)  # 获取窗口文本的字符数
        hwnd = win32gui.FindWindow("Notepad", None)
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)  # 隐藏窗口
        time.sleep(2)
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)  # 显示窗口
        # SW_SHOW：在窗口原来的位置以原来的尺寸激活和显示窗口
        hwnd = win32gui.FindWindow("Notepad", None)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)  # 最大化指定的窗口。nCmdShow=3
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)  # 最小化指定的窗口并且激活在Z序中的下一个顶层窗口。nCmdShow=6
        hwnd = win32gui.FindWindow("Notepad", None)
        win32gui.ShowWindow(
            hwnd, win32con.SW_RESTORE
        )  # 激活并显示窗口。如果窗口最小化或最大化，则系统将窗口恢复到原来的尺寸和位置。在恢复最小化窗口时，应用程序应该指定这个标志。nCmdShow=9
        hwnd = win32gui.FindWindow("Notepad", None)
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)  # 激活窗口并将其最大化。nCmdShow=3
        # SW_SHOWMINIMIZED：激活窗口并将其最小化。nCmdShow=2。
        # SW_SHOWMINNOACTIVE：窗口最小化，激活窗口仍然维持激活状态。nCmdShow=7。
        # SW_SHOWNA：以窗口原来的状态显示窗口。激活窗口仍然维持激活状态。nCmdShow=8。
        # SW_SHOWNOACTIVATE：以窗口最近一次的大小和状态显示窗口。激活窗口仍然维持激活状态。nCmdShow=4。
        # SW_SHOWNORMAL：激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。应用程序在第一次显示窗口的时候应该指定此标志。nCmdShow=1。

        win32api.SetCursorPos([30, 150])  # 鼠标定位到(30,50)--坐标系屏幕
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
        )  # 执行左单键击，若需要双击则延时几毫秒再点击一次即可
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)  # 右键单击

    def initUI(self):
        myWin = Ui_Dialog()
        myWin.setupUi(self)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    login()
    main()
