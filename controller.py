import sys
from ui.mainwindow import *
from PyQt5.QtWidgets import QApplication, QMainWindow

class maincontroller(object):
    def __init__(self):

        self.mainwindow = QMainWindow()
        self.main_ui = mainfunc()
        self.main_ui.setupUi(self.mainwindow)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化主窗口
    main = maincontroller()
    # 显示
    main.mainwindow.show()
    sys.exit(app.exec_())