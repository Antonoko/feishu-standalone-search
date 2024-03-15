import os
import sys
import platform
import win32gui
import win32con

if getattr(sys, 'frozen', False):
    # 如果程序已经被打包
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

import pyautogui
from PyQt5.QtWidgets import QApplication, QLabel, QAction, QMenu
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtGui import QPixmap

# 创建Qt应用
app = QApplication(sys.argv)

# 创建一个Qt Label窗口来承载图片，并设置窗口透明度
imageLabel = QLabel()
imageLabel.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
imageLabel.setAttribute(Qt.WA_TranslucentBackground)
imageLabel.setStyleSheet("background-color:transparent;") 

# 加载png图片
pix_normal = QPixmap(os.path.join(bundle_dir, 'resource','SearchBar.png'))
pix_hover = QPixmap(os.path.join(bundle_dir, 'resource','SearchBar_hover.png'))
# pix_pressed = QPixmap('SearchBar_press.png')
imageLabel.setPixmap(pix_normal)
imageLabel.show()

# 创建 Qt 对象来记录鼠标按下的时间
press_time = QTime()

# 找到飞书来一下
def callFeishuSearch():
    feishu_title = ["Feishu", "飞书", "Lark"]
    for title in feishu_title:
        if platform.system() == "Windows":
            # 在所有窗口中查找标题包含“飞书”的窗口，并切换到前台
            hwnd = win32gui.FindWindow(None, title)
            if hwnd:
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)
                pyautogui.hotkey('ctrl', 'k')
        elif platform.system() == "Darwin":  # macOS
            os.system('''/usr/bin/osascript -e 'tell app "{}" to activate' '''.format(title))
            pyautogui.hotkey('command', 'k')


# 定义鼠标点击事件
def mousePressEvent(event):
    if event.button() == Qt.LeftButton:
        press_time.start()  # 开始计时
        imageLabel.offset = event.pos()
        # imageLabel.setPixmap(pix_pressed) # 设置按下时的图片

# 定义鼠标进入和离开事件
def enterEvent(event):
    imageLabel.setPixmap(pix_hover)  # 设置悬停图片

def leaveEvent(event):
    imageLabel.setPixmap(pix_normal)  # 还原图片

# 定义鼠标移动的事件
def mouseMoveEvent(event):
    x = event.globalX()
    y = event.globalY()
    x_w = imageLabel.offset.x()
    y_w = imageLabel.offset.y()
    imageLabel.move(x - x_w, y - y_w)

# 定义鼠标释放的事件
def mouseReleaseEvent(event):
    if event.button() == Qt.LeftButton:
        t_elapsed = press_time.elapsed() / 100  # 计算按下鼠标到现在过去的时间(秒)

        if t_elapsed < 1:
            callFeishuSearch()

# 定义右键弹出菜单事件
def contextMenuEvent(event):
    contextMenu = QMenu(imageLabel)
    quitAct = QAction("Close", imageLabel)
    quitAct.triggered.connect(app.quit)
    contextMenu.addAction(quitAct)
    contextMenu.exec_(imageLabel.mapToGlobal(event.pos()))


# 显示图片并移动窗口到屏幕指定位置
screen_geo = QApplication.desktop().screenGeometry()
window_geo = imageLabel.geometry()

imageLabel.move(
    ((screen_geo.width() - window_geo.width()) // 2),
    ((screen_geo.height() * 1) // 7)
)

imageLabel.mousePressEvent = mousePressEvent
imageLabel.mouseMoveEvent = mouseMoveEvent
imageLabel.mouseReleaseEvent = mouseReleaseEvent
imageLabel.enterEvent = enterEvent
imageLabel.leaveEvent = leaveEvent
imageLabel.contextMenuEvent = contextMenuEvent




# 运行Qt应用
sys.exit(app.exec_())
