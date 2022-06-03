# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pre.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import pandas as pd
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette,QBrush,QPixmap,QIcon
import qtawesome
import os
import re
from utils.sqlconnect import *
from utils.tushare_stable import *
from utils.feature_engineering import *
from utils.predictionmodel import *
from ui.feature import *
from ui.res import *

class Ui_pre(object):
    def __init__(self):
        self.code=''
        self.name=''
        self.data=None
        self.sql=mysql_conn()
        self.hasdata=False
        self.check=False

    def setupUi(self, pre):
        pre.setObjectName("pre")
        pre.resize(800, 500)
        pre.setFixedSize(pre.width(), pre.height())
        self.pushButton_4 = QtWidgets.QPushButton(pre)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 400, 91, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(pre)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 260, 241, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(pre)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 260, 241, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(pre)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 100, 110, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(pre)
        self.pushButton_8.setGeometry(QtCore.QRect(670, 100, 110, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_3 = QtWidgets.QLabel(pre)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(pre)
        self.label.setGeometry(QtCore.QRect(200, 100, 181, 41))
        self.label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.label.setObjectName("label")
        self.label.setText("")
        self.pushButton_9 = QtWidgets.QPushButton(pre)
        self.pushButton_9.setGeometry(QtCore.QRect(410, 100, 110, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_4.clicked.connect(pre.close)

        self.retranslateUi(pre)
        self.beautify(pre)
        QtCore.QMetaObject.connectSlotsByName(pre)

        self.pushButton_9.clicked.connect(lambda :self.getcode(pre))
        self.pushButton_7.clicked.connect(lambda :self.search(pre))
        self.pushButton_5.clicked.connect(self.autopredict)
        self.pushButton_6.clicked.connect(self.predict_diy)
        self.pushButton_8.clicked.connect(self.update)

    def retranslateUi(self, pre):
        _translate = QtCore.QCoreApplication.translate
        pre.setWindowTitle(_translate("pre", "pre"))
        self.pushButton_4.setText(_translate("pre", "返回"))
        self.pushButton_5.setText(_translate("pre", "自动预测"))
        self.pushButton_6.setText(_translate("pre", "自定义预测"))
        self.pushButton_7.setText(_translate("pre", "数据查询"))
        self.pushButton_8.setText(_translate("pre", "数据更新"))
        self.label_3.setText(_translate("pre", "<html><head/><body><p><span style=\" font-size:18pt;\">股票代号：</span></p></body></html>"))
        self.pushButton_9.setText(_translate("pre", "点击输入"))

    def beautify(self,Form):
        # 利用qtawesome设置图标
        Form.setWindowOpacity(0.95)
        palette = QPalette()
        path = os.path.join('source', 'timg2.jpg')
        palette.setBrush(QPalette.Background, QBrush(QPixmap(path)))
        Form.setPalette(palette)

        # icon
        iconpath = os.path.join('source', 'icon.jpg')
        Form.setWindowIcon(QIcon(iconpath))

        #spin_icon = qtawesome.icon('fa5s.microphone-alt', color='black')
        spin_icon1 = qtawesome.icon('fa.question', color='black')
        spin_icon2 = qtawesome.icon('fa.comment', color='black')
        spin_icon3 = qtawesome.icon('fa5s.ban', color='black')
        spin_icon5 = qtawesome.icon('fa.book', color='black')

        self.pushButton_4.setIcon(spin_icon3)
        self.pushButton_5.setIcon(spin_icon2)
        self.pushButton_6.setIcon(spin_icon2)
        self.pushButton_7.setIcon(spin_icon5)
        self.pushButton_8.setIcon(spin_icon5)
        self.pushButton_9.setIcon(spin_icon5)

        # 设置pushbutton格式
        self.pushButton_4.setStyleSheet('''QPushButton{border:none;}
                                QPushButton:hover{color:white;
                                            border:2px solid #F3F3F5;
                                            border-radius:35px;
                                            background:darkGray;}''')

        self.pushButton_5.setStyleSheet('''QPushButton{border:none;}
                                        QPushButton:hover{color:white;
                                                    border:2px solid #F3F3F5;
                                                    border-radius:35px;
                                                    background:darkGray;}''')

        self.pushButton_6.setStyleSheet('''QPushButton{border:none;}
                                                QPushButton:hover{color:white;
                                                            border:2px solid #F3F3F5;
                                                            border-radius:35px;
                                                            background:darkGray;}''')

        self.pushButton_7.setStyleSheet('''QPushButton{border:none;}
                                                QPushButton:hover{color:white;
                                                            border:2px solid #F3F3F5;
                                                            border-radius:35px;
                                                            background:darkGray;}''')
        self.pushButton_8.setStyleSheet('''QPushButton{border:none;}
                                                        QPushButton:hover{color:white;
                                                                    border:2px solid #F3F3F5;
                                                                    border-radius:35px;
                                                                    background:darkGray;}''')
        self.pushButton_9.setStyleSheet('''QPushButton{border:none;}
                                                        QPushButton:hover{color:white;
                                                                    border:2px solid #F3F3F5;
                                                                    border-radius:35px;
                                                                    background:darkGray;}''')

    def getcode(self,form):
        '''
        输入姓名
        :return: None
        '''
        self.code,ok = QInputDialog.getText(form,"代号","请输入股票代号:",
                                       QLineEdit.Normal,self.label.text())
        if ok and (len(self.code)!=0):
            self.label.setText(self.code)
        self.hasdata=False
        self.name='st'+self.code

    def checkcode(self):
        d=judgegetdaydata(self.code)
        if d==False:
            QMessageBox.about(QWidget(), "提示", '股票代码错误!')
            return False
        else:
            self.check=True
            return True

    def search(self,form):
        '''
        数据查询
        :return:
        '''
        flag=self.checkcode()
        if flag==False:
            return
        else:
            sql = "show tables"
            self.sql.execute_modify_mysql(sql)
            tables = self.sql.cursor.fetchall()
            tables_list = re.findall('(\'.*?\')', str(tables))
            tables_list = [re.sub("'", '', each) for each in tables_list]
            if self.name in tables_list:
                QMessageBox.about(QWidget(), "提示", '数据查询成功!')
                sqldata="select * from "+self.name
                self.data=self.sql.execute_select(sqldata)
                columns1=['open','high','close' ,'low','volume','price_change','p_change','ma5' ,'ma10','ma20' ,'v_ma5','v_ma10','v_ma20','date']
                columns2=['open','high','close' ,'low','volume','price_change','p_change','ma5' ,'ma10','ma20' ,'v_ma5','v_ma10','v_ma20','turnover','date']
                try:
                    self.data = pd.DataFrame(self.data, columns=columns1)
                except:
                    self.data = pd.DataFrame(self.data, columns=columns2)
                self.hasdata=True
            else:
                reply = QMessageBox.question(form, '提示', '数据查询失败，是否进行数据更新？', QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    '''
                   更新数据
                    '''
                    self.update()

    def update(self):
        '''
        数据更新
        :return:
        '''
        flag = self.checkcode()
        if flag == False:
            return
        else:
            self.data=getday(self.code)
            self.data['date']=self.data.index
            sql="DROP TABLE IF EXISTS %s"%(self.name)
            self.sql.execute_modify_mysql(sql)
            '''
            create="""CREATE TABLE IF NOT EXISTS %s(
                            date VARCHAR (255) NOT NULL ,
                            open double(6,4) NOT NULL,
                            high double(6,4) NOT NULL,
                            close double(6,4) NOT NULL,
                            low double(6,4) NOT NULL,
                            volume double(16,2) NOT NULL,
                            price_change double(6,4) NOT NULL,
                            ma5 double(16,2) NOT NULL,
                            ma10 double(16,2) NOT NULL,
                            ma20 double(16,2) NOT NULL,
                            v_ma5 double(16,2) NOT NULL,
                            v_ma10 double(16,2) NOT NULL,
                            v_ma20 double(16,2) NOT NULL,
                            PRIMARY KEY (date))"""%(self.name)

            self.sql.execute_modify_mysql(create)
            '''

            self.data.to_sql(name=self.name, con=self.sql.engine, if_exists='append', index=False, index_label=False)

            self.hasdata=True
            QMessageBox.about(QWidget(), "提示", '数据更新成功!')

    def autopredict(self):
        '''
        自动预测
        :return:
        '''
        if self.hasdata==True:
            '''
            auto predict  连接结果界面
            '''
            self.data = self.data.dropna()
            if 'date' in self.data.columns:
                self.data.drop(['date'], axis=1, inplace=True)
            self.data = self.data.iloc[::-1]
            self.data = self.data.reset_index()
            self.data.drop(columns=['index'], axis=1, inplace=True)
            basicfeature(self.data)

            self.data = self.data.dropna()
            binaryY = makey(self.data)
            model='BP neural network'
            #自动预测使用集成学习模型
            self.resfunc = QWidget()
            self.res = Ui_res()
            self.res.setupUi(self.resfunc, self.data,binaryY,model)
            self.resfunc.show()

        else:
            QMessageBox.about(QWidget(), "提示", '暂无数据或股票代码输入错误!')

    def predict_diy(self):
        '''
        自定义预测
        :return:
        '''
        if self.hasdata==True:
            '''
            连接自定义查询界面
            '''
            self.featurefunc = QWidget()
            self.fe = Ui_feature()
            self.fe.setupUi(self.featurefunc,self.data)
            self.featurefunc.show()
        else:
            QMessageBox.about(QWidget(), "提示", '暂无数据或股票代码输入错误!')
