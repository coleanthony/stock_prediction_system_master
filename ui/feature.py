# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feature.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette,QBrush,QPixmap,QIcon
import qtawesome
import os
import pandas as pd
from utils.predictionmodel import *
from utils.feature_engineering import *
from utils.get_text import *
from ui.res import *

class Ui_feature(object):
    def setupUi(self, Form,data):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        Form.setFixedSize(Form.width(), Form.height())

        self.data=data

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(20, 50, 131, 19))
        self.checkBox.setObjectName("checkBox")
        self.feature = QtWidgets.QLabel(Form)
        self.feature.setGeometry(QtCore.QRect(312, 10, 181, 31))
        self.feature.setObjectName("feature")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 70, 141, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 90, 141, 19))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 110, 91, 19))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 130, 91, 19))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 150, 91, 19))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 170, 91, 19))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Form)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 190, 91, 19))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Form)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 210, 111, 19))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(Form)
        self.checkBox_10.setGeometry(QtCore.QRect(20, 230, 91, 19))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(Form)
        self.checkBox_11.setGeometry(QtCore.QRect(20, 250, 91, 19))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(Form)
        self.checkBox_12.setGeometry(QtCore.QRect(20, 270, 91, 19))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(Form)
        self.checkBox_13.setGeometry(QtCore.QRect(20, 290, 91, 19))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(Form)
        self.checkBox_14.setGeometry(QtCore.QRect(20, 310, 91, 19))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(Form)
        self.checkBox_15.setGeometry(QtCore.QRect(20, 430, 91, 19))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(Form)
        self.checkBox_16.setGeometry(QtCore.QRect(20, 450, 91, 19))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(Form)
        self.checkBox_17.setGeometry(QtCore.QRect(20, 330, 91, 19))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(Form)
        self.checkBox_18.setGeometry(QtCore.QRect(20, 470, 91, 19))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(Form)
        self.checkBox_19.setGeometry(QtCore.QRect(20, 370, 91, 19))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(Form)
        self.checkBox_20.setGeometry(QtCore.QRect(20, 390, 111, 19))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(Form)
        self.checkBox_21.setGeometry(QtCore.QRect(20, 350, 91, 19))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(Form)
        self.checkBox_22.setGeometry(QtCore.QRect(20, 410, 111, 19))
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_23 = QtWidgets.QCheckBox(Form)
        self.checkBox_23.setGeometry(QtCore.QRect(180, 190, 91, 19))
        self.checkBox_23.setObjectName("checkBox_23")
        self.checkBox_24 = QtWidgets.QCheckBox(Form)
        self.checkBox_24.setGeometry(QtCore.QRect(180, 70, 91, 19))
        self.checkBox_24.setObjectName("checkBox_24")
        self.checkBox_25 = QtWidgets.QCheckBox(Form)
        self.checkBox_25.setGeometry(QtCore.QRect(180, 150, 91, 19))
        self.checkBox_25.setObjectName("checkBox_25")
        self.checkBox_26 = QtWidgets.QCheckBox(Form)
        self.checkBox_26.setGeometry(QtCore.QRect(180, 170, 91, 19))
        self.checkBox_26.setObjectName("checkBox_26")
        self.checkBox_27 = QtWidgets.QCheckBox(Form)
        self.checkBox_27.setGeometry(QtCore.QRect(180, 90, 91, 19))
        self.checkBox_27.setObjectName("checkBox_27")
        self.checkBox_28 = QtWidgets.QCheckBox(Form)
        self.checkBox_28.setGeometry(QtCore.QRect(180, 130, 91, 19))
        self.checkBox_28.setObjectName("checkBox_28")
        self.checkBox_29 = QtWidgets.QCheckBox(Form)
        self.checkBox_29.setGeometry(QtCore.QRect(180, 50, 91, 19))
        self.checkBox_29.setObjectName("checkBox_29")
        self.checkBox_30 = QtWidgets.QCheckBox(Form)
        self.checkBox_30.setGeometry(QtCore.QRect(180, 110, 91, 19))
        self.checkBox_30.setObjectName("checkBox_30")
        self.checkBox_31 = QtWidgets.QCheckBox(Form)
        self.checkBox_31.setGeometry(QtCore.QRect(180, 210, 91, 19))
        self.checkBox_31.setObjectName("checkBox_31")
        self.checkBox_32 = QtWidgets.QCheckBox(Form)
        self.checkBox_32.setGeometry(QtCore.QRect(180, 250, 91, 19))
        self.checkBox_32.setObjectName("checkBox_32")
        self.checkBox_33 = QtWidgets.QCheckBox(Form)
        self.checkBox_33.setGeometry(QtCore.QRect(180, 310, 91, 19))
        self.checkBox_33.setObjectName("checkBox_33")
        self.checkBox_34 = QtWidgets.QCheckBox(Form)
        self.checkBox_34.setGeometry(QtCore.QRect(180, 330, 91, 19))
        self.checkBox_34.setObjectName("checkBox_34")
        self.checkBox_35 = QtWidgets.QCheckBox(Form)
        self.checkBox_35.setGeometry(QtCore.QRect(180, 350, 91, 19))
        self.checkBox_35.setObjectName("checkBox_35")
        self.checkBox_36 = QtWidgets.QCheckBox(Form)
        self.checkBox_36.setGeometry(QtCore.QRect(180, 290, 111, 19))
        self.checkBox_36.setObjectName("checkBox_36")
        self.checkBox_37 = QtWidgets.QCheckBox(Form)
        self.checkBox_37.setGeometry(QtCore.QRect(180, 270, 91, 19))
        self.checkBox_37.setObjectName("checkBox_37")
        self.checkBox_38 = QtWidgets.QCheckBox(Form)
        self.checkBox_38.setGeometry(QtCore.QRect(180, 230, 91, 19))
        self.checkBox_38.setObjectName("checkBox_38")
        self.checkBox_39 = QtWidgets.QCheckBox(Form)
        self.checkBox_39.setGeometry(QtCore.QRect(180, 370, 91, 19))
        self.checkBox_39.setObjectName("checkBox_39")
        self.checkBox_40 = QtWidgets.QCheckBox(Form)
        self.checkBox_40.setGeometry(QtCore.QRect(180, 410, 91, 19))
        self.checkBox_40.setObjectName("checkBox_40")
        self.checkBox_41 = QtWidgets.QCheckBox(Form)
        self.checkBox_41.setGeometry(QtCore.QRect(180, 470, 101, 19))
        self.checkBox_41.setObjectName("checkBox_41")
        self.checkBox_44 = QtWidgets.QCheckBox(Form)
        self.checkBox_44.setGeometry(QtCore.QRect(180, 450, 91, 19))
        self.checkBox_44.setObjectName("checkBox_44")
        self.checkBox_45 = QtWidgets.QCheckBox(Form)
        self.checkBox_45.setGeometry(QtCore.QRect(180, 430, 91, 19))
        self.checkBox_45.setObjectName("checkBox_45")
        self.checkBox_46 = QtWidgets.QCheckBox(Form)
        self.checkBox_46.setGeometry(QtCore.QRect(180, 390, 91, 19))
        self.checkBox_46.setObjectName("checkBox_46")
        self.checkBox_42 = QtWidgets.QCheckBox(Form)
        self.checkBox_42.setGeometry(QtCore.QRect(330, 350, 121, 19))
        self.checkBox_42.setObjectName("checkBox_42")
        self.checkBox_43 = QtWidgets.QCheckBox(Form)
        self.checkBox_43.setGeometry(QtCore.QRect(330, 470, 91, 19))
        self.checkBox_43.setObjectName("checkBox_43")
        self.checkBox_47 = QtWidgets.QCheckBox(Form)
        self.checkBox_47.setGeometry(QtCore.QRect(330, 410, 91, 19))
        self.checkBox_47.setObjectName("checkBox_47")
        self.checkBox_48 = QtWidgets.QCheckBox(Form)
        self.checkBox_48.setGeometry(QtCore.QRect(330, 110, 91, 19))
        self.checkBox_48.setObjectName("checkBox_48")
        self.checkBox_49 = QtWidgets.QCheckBox(Form)
        self.checkBox_49.setGeometry(QtCore.QRect(330, 450, 91, 19))
        self.checkBox_49.setObjectName("checkBox_49")
        self.checkBox_50 = QtWidgets.QCheckBox(Form)
        self.checkBox_50.setGeometry(QtCore.QRect(330, 230, 91, 19))
        self.checkBox_50.setObjectName("checkBox_50")
        self.checkBox_51 = QtWidgets.QCheckBox(Form)
        self.checkBox_51.setGeometry(QtCore.QRect(330, 430, 121, 19))
        self.checkBox_51.setObjectName("checkBox_51")
        self.checkBox_52 = QtWidgets.QCheckBox(Form)
        self.checkBox_52.setGeometry(QtCore.QRect(330, 290, 91, 19))
        self.checkBox_52.setObjectName("checkBox_52")
        self.checkBox_53 = QtWidgets.QCheckBox(Form)
        self.checkBox_53.setGeometry(QtCore.QRect(330, 170, 91, 19))
        self.checkBox_53.setObjectName("checkBox_53")
        self.checkBox_54 = QtWidgets.QCheckBox(Form)
        self.checkBox_54.setGeometry(QtCore.QRect(330, 270, 91, 19))
        self.checkBox_54.setObjectName("checkBox_54")
        self.checkBox_55 = QtWidgets.QCheckBox(Form)
        self.checkBox_55.setGeometry(QtCore.QRect(330, 370, 111, 19))
        self.checkBox_55.setObjectName("checkBox_55")
        self.checkBox_56 = QtWidgets.QCheckBox(Form)
        self.checkBox_56.setGeometry(QtCore.QRect(330, 190, 91, 19))
        self.checkBox_56.setObjectName("checkBox_56")
        self.checkBox_57 = QtWidgets.QCheckBox(Form)
        self.checkBox_57.setGeometry(QtCore.QRect(330, 150, 91, 19))
        self.checkBox_57.setObjectName("checkBox_57")
        self.checkBox_58 = QtWidgets.QCheckBox(Form)
        self.checkBox_58.setGeometry(QtCore.QRect(330, 330, 91, 19))
        self.checkBox_58.setObjectName("checkBox_58")
        self.checkBox_59 = QtWidgets.QCheckBox(Form)
        self.checkBox_59.setGeometry(QtCore.QRect(330, 90, 91, 19))
        self.checkBox_59.setObjectName("checkBox_59")
        self.checkBox_60 = QtWidgets.QCheckBox(Form)
        self.checkBox_60.setGeometry(QtCore.QRect(330, 310, 91, 19))
        self.checkBox_60.setObjectName("checkBox_60")
        self.checkBox_61 = QtWidgets.QCheckBox(Form)
        self.checkBox_61.setGeometry(QtCore.QRect(330, 70, 91, 19))
        self.checkBox_61.setObjectName("checkBox_61")
        self.checkBox_62 = QtWidgets.QCheckBox(Form)
        self.checkBox_62.setGeometry(QtCore.QRect(330, 390, 101, 19))
        self.checkBox_62.setObjectName("checkBox_62")
        self.checkBox_63 = QtWidgets.QCheckBox(Form)
        self.checkBox_63.setGeometry(QtCore.QRect(330, 50, 111, 19))
        self.checkBox_63.setObjectName("checkBox_63")
        self.checkBox_64 = QtWidgets.QCheckBox(Form)
        self.checkBox_64.setGeometry(QtCore.QRect(330, 250, 91, 19))
        self.checkBox_64.setObjectName("checkBox_64")
        self.checkBox_65 = QtWidgets.QCheckBox(Form)
        self.checkBox_65.setGeometry(QtCore.QRect(330, 210, 91, 19))
        self.checkBox_65.setObjectName("checkBox_65")
        self.checkBox_66 = QtWidgets.QCheckBox(Form)
        self.checkBox_66.setGeometry(QtCore.QRect(330, 130, 91, 19))
        self.checkBox_66.setObjectName("checkBox_66")
        self.checkBox_67 = QtWidgets.QCheckBox(Form)
        self.checkBox_67.setGeometry(QtCore.QRect(490, 470, 91, 19))
        self.checkBox_67.setObjectName("checkBox_67")
        self.checkBox_68 = QtWidgets.QCheckBox(Form)
        self.checkBox_68.setGeometry(QtCore.QRect(490, 370, 91, 19))
        self.checkBox_68.setObjectName("checkBox_68")
        self.checkBox_69 = QtWidgets.QCheckBox(Form)
        self.checkBox_69.setGeometry(QtCore.QRect(490, 390, 91, 19))
        self.checkBox_69.setObjectName("checkBox_69")
        self.checkBox_70 = QtWidgets.QCheckBox(Form)
        self.checkBox_70.setGeometry(QtCore.QRect(490, 110, 171, 19))
        self.checkBox_70.setObjectName("checkBox_70")
        self.checkBox_71 = QtWidgets.QCheckBox(Form)
        self.checkBox_71.setGeometry(QtCore.QRect(490, 250, 91, 19))
        self.checkBox_71.setObjectName("checkBox_71")
        self.checkBox_72 = QtWidgets.QCheckBox(Form)
        self.checkBox_72.setGeometry(QtCore.QRect(490, 70, 161, 19))
        self.checkBox_72.setObjectName("checkBox_72")
        self.checkBox_73 = QtWidgets.QCheckBox(Form)
        self.checkBox_73.setGeometry(QtCore.QRect(490, 350, 91, 19))
        self.checkBox_73.setObjectName("checkBox_73")
        self.checkBox_74 = QtWidgets.QCheckBox(Form)
        self.checkBox_74.setGeometry(QtCore.QRect(490, 330, 121, 19))
        self.checkBox_74.setObjectName("checkBox_74")
        self.checkBox_75 = QtWidgets.QCheckBox(Form)
        self.checkBox_75.setGeometry(QtCore.QRect(490, 450, 91, 19))
        self.checkBox_75.setObjectName("checkBox_75")
        self.checkBox_76 = QtWidgets.QCheckBox(Form)
        self.checkBox_76.setGeometry(QtCore.QRect(490, 270, 91, 19))
        self.checkBox_76.setObjectName("checkBox_76")
        self.checkBox_77 = QtWidgets.QCheckBox(Form)
        self.checkBox_77.setGeometry(QtCore.QRect(490, 130, 91, 19))
        self.checkBox_77.setObjectName("checkBox_77")
        self.checkBox_78 = QtWidgets.QCheckBox(Form)
        self.checkBox_78.setGeometry(QtCore.QRect(490, 150, 91, 19))
        self.checkBox_78.setObjectName("checkBox_78")
        self.checkBox_79 = QtWidgets.QCheckBox(Form)
        self.checkBox_79.setGeometry(QtCore.QRect(490, 50, 121, 19))
        self.checkBox_79.setObjectName("checkBox_79")
        self.checkBox_80 = QtWidgets.QCheckBox(Form)
        self.checkBox_80.setGeometry(QtCore.QRect(490, 430, 91, 19))
        self.checkBox_80.setObjectName("checkBox_80")
        self.checkBox_81 = QtWidgets.QCheckBox(Form)
        self.checkBox_81.setGeometry(QtCore.QRect(490, 310, 91, 19))
        self.checkBox_81.setObjectName("checkBox_81")
        self.checkBox_82 = QtWidgets.QCheckBox(Form)
        self.checkBox_82.setGeometry(QtCore.QRect(490, 230, 91, 19))
        self.checkBox_82.setObjectName("checkBox_82")
        self.checkBox_83 = QtWidgets.QCheckBox(Form)
        self.checkBox_83.setGeometry(QtCore.QRect(490, 190, 91, 19))
        self.checkBox_83.setObjectName("checkBox_83")
        self.checkBox_84 = QtWidgets.QCheckBox(Form)
        self.checkBox_84.setGeometry(QtCore.QRect(490, 290, 91, 19))
        self.checkBox_84.setObjectName("checkBox_84")
        self.checkBox_85 = QtWidgets.QCheckBox(Form)
        self.checkBox_85.setGeometry(QtCore.QRect(490, 90, 171, 19))
        self.checkBox_85.setObjectName("checkBox_85")
        self.checkBox_86 = QtWidgets.QCheckBox(Form)
        self.checkBox_86.setGeometry(QtCore.QRect(490, 210, 91, 19))
        self.checkBox_86.setObjectName("checkBox_86")
        self.checkBox_87 = QtWidgets.QCheckBox(Form)
        self.checkBox_87.setGeometry(QtCore.QRect(490, 170, 91, 19))
        self.checkBox_87.setObjectName("checkBox_87")
        self.checkBox_88 = QtWidgets.QCheckBox(Form)
        self.checkBox_88.setGeometry(QtCore.QRect(490, 410, 91, 19))
        self.checkBox_88.setObjectName("checkBox_88")
        self.checkBox_91 = QtWidgets.QCheckBox(Form)
        self.checkBox_91.setGeometry(QtCore.QRect(670, 70, 91, 19))
        self.checkBox_91.setObjectName("checkBox_91")
        self.checkBox_92 = QtWidgets.QCheckBox(Form)
        self.checkBox_92.setGeometry(QtCore.QRect(670, 130, 91, 19))
        self.checkBox_92.setObjectName("checkBox_92")
        self.checkBox_93 = QtWidgets.QCheckBox(Form)
        self.checkBox_93.setGeometry(QtCore.QRect(670, 110, 91, 19))
        self.checkBox_93.setObjectName("checkBox_93")
        self.checkBox_96 = QtWidgets.QCheckBox(Form)
        self.checkBox_96.setGeometry(QtCore.QRect(670, 150, 91, 19))
        self.checkBox_96.setObjectName("checkBox_96")
        self.checkBox_97 = QtWidgets.QCheckBox(Form)
        self.checkBox_97.setGeometry(QtCore.QRect(670, 90, 91, 19))
        self.checkBox_97.setObjectName("checkBox_97")
        self.checkBox_100 = QtWidgets.QCheckBox(Form)
        self.checkBox_100.setGeometry(QtCore.QRect(670, 50, 121, 19))
        self.checkBox_100.setObjectName("checkBox_100")
        self.checkBox_101 = QtWidgets.QCheckBox(Form)
        self.checkBox_101.setGeometry(QtCore.QRect(670, 210, 91, 19))
        self.checkBox_101.setObjectName("checkBox_101")
        self.checkBox_102 = QtWidgets.QCheckBox(Form)
        self.checkBox_102.setGeometry(QtCore.QRect(670, 170, 91, 19))
        self.checkBox_102.setObjectName("checkBox_102")
        self.checkBox_106 = QtWidgets.QCheckBox(Form)
        self.checkBox_106.setGeometry(QtCore.QRect(670, 190, 121, 19))
        self.checkBox_106.setObjectName("checkBox_106")
        self.checkBox_107 = QtWidgets.QCheckBox(Form)
        self.checkBox_107.setGeometry(QtCore.QRect(670, 250, 121, 19))
        self.checkBox_107.setObjectName("checkBox_107")
        self.checkBox_108 = QtWidgets.QCheckBox(Form)
        self.checkBox_108.setGeometry(QtCore.QRect(670, 230, 91, 19))
        self.checkBox_108.setObjectName("checkBox_108")
        self.checkBox_109 = QtWidgets.QCheckBox(Form)
        self.checkBox_109.setGeometry(QtCore.QRect(670, 270, 121, 19))
        self.checkBox_109.setObjectName("checkBox_109")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 320, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 400, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton.clicked.connect(lambda :self.model_selection(Form))

        self.beautify(Form)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "feature"))
        self.checkBox.setText(_translate("Form", "BBAMDS_bands5"))
        self.feature.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffaa00;\">STOCK</span></p></body></html>"))
        self.checkBox_2.setText(_translate("Form", "BBAMDS_bands15"))
        self.checkBox_3.setText(_translate("Form", "BBAMDS_bands30"))
        self.checkBox_4.setText(_translate("Form", "DEMA_7"))
        self.checkBox_5.setText(_translate("Form", "DEMA_15"))
        self.checkBox_6.setText(_translate("Form", "DEMA_30"))
        self.checkBox_7.setText(_translate("Form", "EMA12"))
        self.checkBox_8.setText(_translate("Form", "EMA30"))
        self.checkBox_9.setText(_translate("Form", "HTTRENDLINE"))
        self.checkBox_10.setText(_translate("Form", "kama7"))
        self.checkBox_11.setText(_translate("Form", "kama20"))
        self.checkBox_12.setText(_translate("Form", "kama30"))
        self.checkBox_13.setText(_translate("Form", "MA5"))
        self.checkBox_14.setText(_translate("Form", "MA10"))
        self.checkBox_15.setText(_translate("Form", "SAR"))
        self.checkBox_16.setText(_translate("Form", "sarext"))
        self.checkBox_17.setText(_translate("Form", "MA20"))
        self.checkBox_18.setText(_translate("Form", "SMA7"))
        self.checkBox_19.setText(_translate("Form", "MAMA"))
        self.checkBox_20.setText(_translate("Form", "minpoint14"))
        self.checkBox_21.setText(_translate("Form", "MA30"))
        self.checkBox_22.setText(_translate("Form", "midprice14"))
        self.checkBox_23.setText(_translate("Form", "WMA30"))
        self.checkBox_24.setText(_translate("Form", "SMA30"))
        self.checkBox_25.setText(_translate("Form", "TEMA30"))
        self.checkBox_26.setText(_translate("Form", "trima30"))
        self.checkBox_27.setText(_translate("Form", "T3"))
        self.checkBox_28.setText(_translate("Form", "TEMA15"))
        self.checkBox_29.setText(_translate("Form", "SMA15"))
        self.checkBox_30.setText(_translate("Form", "TEMA5"))
        self.checkBox_31.setText(_translate("Form", "ADX14"))
        self.checkBox_32.setText(_translate("Form", "APO"))
        self.checkBox_33.setText(_translate("Form", "BOP"))
        self.checkBox_34.setText(_translate("Form", "CCI14"))
        self.checkBox_35.setText(_translate("Form", "CMO14"))
        self.checkBox_36.setText(_translate("Form", "Aroonosc14"))
        self.checkBox_37.setText(_translate("Form", "Aroon14"))
        self.checkBox_38.setText(_translate("Form", "ADXR14"))
        self.checkBox_39.setText(_translate("Form", "DX14"))
        self.checkBox_40.setText(_translate("Form", "MACTEXT"))
        self.checkBox_41.setText(_translate("Form", "MINUS_DI14"))
        self.checkBox_44.setText(_translate("Form", "MFI14"))
        self.checkBox_45.setText(_translate("Form", "MACDFIX"))
        self.checkBox_46.setText(_translate("Form", "MACD"))
        self.checkBox_42.setText(_translate("Form", "HT_DCPERIOD"))
        self.checkBox_43.setText(_translate("Form", "CORREL30"))
        self.checkBox_47.setText(_translate("Form", "HT_SINE"))
        self.checkBox_48.setText(_translate("Form", "MOM10"))
        self.checkBox_49.setText(_translate("Form", "BETA"))
        self.checkBox_50.setText(_translate("Form", "NATR14"))
        self.checkBox_51.setText(_translate("Form", "HT_TRENDMODE"))
        self.checkBox_52.setText(_translate("Form", "MEDPRICE"))
        self.checkBox_53.setText(_translate("Form", "ADOSC"))
        self.checkBox_54.setText(_translate("Form", "avgprice"))
        self.checkBox_55.setText(_translate("Form", "HT_DCPHASE"))
        self.checkBox_56.setText(_translate("Form", "OBV"))
        self.checkBox_57.setText(_translate("Form", "AD"))
        self.checkBox_58.setText(_translate("Form", "WCLPRICE"))
        self.checkBox_59.setText(_translate("Form", "MOM20"))
        self.checkBox_60.setText(_translate("Form", "TYPPRICE"))
        self.checkBox_61.setText(_translate("Form", "MOM30"))
        self.checkBox_62.setText(_translate("Form", "HT_PHASOR"))
        self.checkBox_63.setText(_translate("Form", "MINUS_DM14"))
        self.checkBox_64.setText(_translate("Form", "TRANGE"))
        self.checkBox_65.setText(_translate("Form", "ATR14"))
        self.checkBox_66.setText(_translate("Form", "RSI14"))
        self.checkBox_67.setText(_translate("Form", "tanh"))
        self.checkBox_68.setText(_translate("Form", "log10"))
        self.checkBox_69.setText(_translate("Form", "sin"))
        self.checkBox_70.setText(_translate("Form", "LINEARREG_SLOPE14"))
        self.checkBox_71.setText(_translate("Form", "vecceil"))
        self.checkBox_72.setText(_translate("Form", "LINEARREG_ANGLE14"))
        self.checkBox_73.setText(_translate("Form", "LN"))
        self.checkBox_74.setText(_translate("Form", "vectorfloor"))
        self.checkBox_75.setText(_translate("Form", "tan"))
        self.checkBox_76.setText(_translate("Form", "cos"))
        self.checkBox_77.setText(_translate("Form", "stddev5"))
        self.checkBox_78.setText(_translate("Form", "TSF14"))
        self.checkBox_79.setText(_translate("Form", "LINEARREG14"))
        self.checkBox_80.setText(_translate("Form", "sqrt"))
        self.checkBox_81.setText(_translate("Form", "vexp"))
        self.checkBox_82.setText(_translate("Form", "atan"))
        self.checkBox_83.setText(_translate("Form", "acos"))
        self.checkBox_84.setText(_translate("Form", "cosh"))
        self.checkBox_85.setText(_translate("Form", "LINEARREG_INTERCEPT14"))
        self.checkBox_86.setText(_translate("Form", "asin"))
        self.checkBox_87.setText(_translate("Form", "VAR5"))
        self.checkBox_88.setText(_translate("Form", "sinh"))
        self.checkBox_91.setText(_translate("Form", "div"))
        self.checkBox_92.setText(_translate("Form", "lowest"))
        self.checkBox_93.setText(_translate("Form", "maxindex"))
        self.checkBox_96.setText(_translate("Form", "minindex"))
        self.checkBox_97.setText(_translate("Form", "highest"))
        self.checkBox_100.setText(_translate("Form", "add"))
        self.checkBox_101.setText(_translate("Form", "multy"))
        self.checkBox_102.setText(_translate("Form", "minmax"))
        self.checkBox_106.setText(_translate("Form", "minmaxindex"))
        self.checkBox_107.setText(_translate("Form", "summation30"))
        self.checkBox_108.setText(_translate("Form", "subtra"))
        self.checkBox_109.setText(_translate("Form", "添加语义分析"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">feature selection</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "模型选择"))
        self.pushButton_2.setText(_translate("Form", "返回"))

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

        spin_icon3 = qtawesome.icon('fa5s.ban', color='black')
        spin_icon5 = qtawesome.icon('fa.book', color='black')
        self.pushButton.setIcon(spin_icon5)
        self.pushButton_2.setIcon(spin_icon3)

        # 设置pushbutton格式
        self.pushButton.setStyleSheet('''QPushButton{border:none;}
                                QPushButton:hover{color:white;
                                            border:2px solid #F3F3F5;
                                            border-radius:35px;
                                            background:darkGray;}''')

        self.pushButton_2.setStyleSheet('''QPushButton{border:none;}
                                        QPushButton:hover{color:white;
                                                    border:2px solid #F3F3F5;
                                                    border-radius:35px;
                                                    background:darkGray;}''')

    def model_selection(self,form):
        '''
        选择模型
        :return:
        '''
        list = ['SVM', 'random forest', 'SGD', 'XGBoost', 'Adaboost', 'Bagging random forest', 'BP neural network', 'LSTM neural network', 'Multilayer LSTM','LSTM ensemble']
        self.model, ok = QInputDialog.getItem(form, "模型", "请选择模型：", list)
        if ok:
            reply = QMessageBox.question(form, '提示', '模型选择完成，是否进行预测？', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                date = self.data['date'].values
                if 'date' in self.data.columns:
                    self.data.drop(['date'], axis=1, inplace=True)
                self.data = self.data.iloc[::-1]
                self.data = self.data.reset_index()
                if 'index' in self.data.columns:
                    self.data.drop(columns=['index'], axis=1,inplace=True)

                self.check()
                self.data = self.data.dropna()

                binaryY=makey(self.data)

                pos = self.check_NLP(date, form)
                if pos:
                    pos=pos.reverse()
                    self.data['pos']=pd.DataFrame(pos)

                self.resfunc = QWidget()
                self.res = Ui_res()
                self.res.setupUi(self.resfunc, self.data, binaryY, self.model)
                self.resfunc.show()

    def check(self):
        if self.checkBox.isChecked():
            BBAMDS_bands5(self.data)

        if self.checkBox_2.isChecked():
            BBAMDS_bands15(self.data)

        if self.checkBox_3.isChecked():
            BBAMDS_bands30(self.data)

        if self.checkBox_4.isChecked():
            DEMA_7(self.data)

        if self.checkBox_5.isChecked():
            DEMA_15(self.data)

        if self.checkBox_6.isChecked():
            DEMA_30(self.data)

        if self.checkBox_7.isChecked():
            EMA12(self.data)

        if self.checkBox_8.isChecked():
            EMA30(self.data)

        if self.checkBox_9.isChecked():
            HTTRENDLINE(self.data)

        if self.checkBox_10.isChecked():
            kama7(self.data)

        if self.checkBox_11.isChecked():
            kama20(self.data)

        if self.checkBox_12.isChecked():
            kama30(self.data)

        if self.checkBox_13.isChecked():
            MA5(self.data)

        if self.checkBox_14.isChecked():
            MA10(self.data)

        if self.checkBox_15.isChecked():
            SAR0(self.data)

        if self.checkBox_16.isChecked():
            sarext(self.data)

        if self.checkBox_17.isChecked():
            MA20(self.data)

        if self.checkBox_18.isChecked():
            SMA7(self.data)

        if self.checkBox_19.isChecked():
            MAMA0(self.data)

        if self.checkBox_20.isChecked():
            minpoint14(self.data)

        if self.checkBox_21.isChecked():
            MA30(self.data)

        if self.checkBox_22.isChecked():
            midprice14(self.data)

        if self.checkBox_23.isChecked():
            WMA30(self.data)

        if self.checkBox_24.isChecked():
            SMA30(self.data)

        if self.checkBox_25.isChecked():
            TEMA30(self.data)

        if self.checkBox_26.isChecked():
            trima30(self.data)

        if self.checkBox_27.isChecked():
            T35(self.data)

        if self.checkBox_28.isChecked():
            TEMA15(self.data)

        if self.checkBox_29.isChecked():
            SMA15(self.data)

        if self.checkBox_30.isChecked():
            TEMA5(self.data)

        if self.checkBox_31.isChecked():
            ADX14(self.data)

        if self.checkBox_32.isChecked():
            APO12(self.data)

        if self.checkBox_33.isChecked():
            BOP0(self.data)

        if self.checkBox_34.isChecked():
            CCI14(self.data)

        if self.checkBox_35.isChecked():
            CMO14(self.data)

        if self.checkBox_36.isChecked():
            Aroonosc14(self.data)

        if self.checkBox_37.isChecked():
            Aroon14(self.data)

        if self.checkBox_38.isChecked():
            ADXR14(self.data)

        if self.checkBox_39.isChecked():
            DX14(self.data)

        if self.checkBox_40.isChecked():
            MACTEXT0(self.data)

        if self.checkBox_41.isChecked():
            MINUS_DI14(self.data)

        if self.checkBox_42.isChecked():
            HT_DCPERIOD(self.data)

        if self.checkBox_43.isChecked():
            CORREL30(self.data)

        if self.checkBox_44.isChecked():
            MFI14(self.data)

        if self.checkBox_45.isChecked():
            MACDFIX0(self.data)

        if self.checkBox_46.isChecked():
            MACD0(self.data)

        if self.checkBox_47.isChecked():
            HT_SINE(self.data)

        if self.checkBox_48.isChecked():
            MOM10(self.data)

        if self.checkBox_49.isChecked():
            BETA0(self.data)

        if self.checkBox_50.isChecked():
            NATR14(self.data)

        if self.checkBox_51.isChecked():
            HT_TRENDMODE(self.data)

        if self.checkBox_52.isChecked():
            MEDPRICE0(self.data)

        if self.checkBox_53.isChecked():
            ADOSC0(self.data)

        if self.checkBox_54.isChecked():
            avgprice(self.data)

        if self.checkBox_55.isChecked():
            HT_DCPHASE(self.data)

        if self.checkBox_56.isChecked():
            OBV0(self.data)

        if self.checkBox_57.isChecked():
            AD0(self.data)

        if self.checkBox_58.isChecked():
            WCLPRICE0(self.data)

        if self.checkBox_59.isChecked():
            MOM20(self.data)

        if self.checkBox_60.isChecked():
            TYPPRICE0(self.data)

        if self.checkBox_61.isChecked():
            MOM30(self.data)

        if self.checkBox_62.isChecked():
            HT_PHASOR(self.data)

        if self.checkBox_63.isChecked():
            MINUS_DM14(self.data)

        if self.checkBox_64.isChecked():
            TRANGE0(self.data)

        if self.checkBox_65.isChecked():
            ATR14(self.data)

        if self.checkBox_66.isChecked():
            RSI14(self.data)

        if self.checkBox_67.isChecked():
            tanh(self.data)

        if self.checkBox_68.isChecked():
            log10(self.data)

        if self.checkBox_69.isChecked():
            sin(self.data)

        if self.checkBox_70.isChecked():
            LINEARREG_SLOPE14(self.data)

        if self.checkBox_71.isChecked():
            vecceil(self.data)

        if self.checkBox_72.isChecked():
            LINEARREG_ANGLE14(self.data)

        if self.checkBox_73.isChecked():
            LN0(self.data)

        if self.checkBox_74.isChecked():
            vectorfloor(self.data)

        if self.checkBox_75.isChecked():
            tan(self.data)

        if self.checkBox_76.isChecked():
            cos(self.data)

        if self.checkBox_77.isChecked():
            stddev5(self.data)

        if self.checkBox_78.isChecked():
            TSF14(self.data)

        if self.checkBox_79.isChecked():
            LINEARREG14(self.data)

        if self.checkBox_80.isChecked():
            sqrt(self.data)

        if self.checkBox_81.isChecked():
            vexp(self.data)

        if self.checkBox_82.isChecked():
            atan(self.data)

        if self.checkBox_83.isChecked():
            acos(self.data)

        if self.checkBox_84.isChecked():
            cosh(self.data)

        if self.checkBox_85.isChecked():
            LINEARREG_INTERCEPT14(self.data)

        if self.checkBox_86.isChecked():
            asin(self.data)

        if self.checkBox_87.isChecked():
            VAR5(self.data)

        if self.checkBox_88.isChecked():
            sinh(self.data)

        if self.checkBox_91.isChecked():
            div(self.data)

        if self.checkBox_92.isChecked():
            lowest(self.data)

        if self.checkBox_93.isChecked():
            maxindex(self.data)

        if self.checkBox_96.isChecked():
            minindex(self.data)

        if self.checkBox_97.isChecked():
            highest(self.data)

        if self.checkBox_100.isChecked():
            add(self.data)

        if self.checkBox_101.isChecked():
            multy(self.data)

        if self.checkBox_102.isChecked():
            minmax(self.data)

        if self.checkBox_106.isChecked():
            minmaxindex(self.data)

        if self.checkBox_107.isChecked():
            summation30(self.data)

        if self.checkBox_108.isChecked():
            subtra(self.data)

    def check_NLP(self,date,form):
        if self.checkBox_109.isChecked():
            '''
            '''
            name, ok = QInputDialog.getText(form, "名称", "请输入查询关键字:",QLineEdit.Normal)
            if ok and (len(name) != 0):
                m=gettext(date,name)
                return m
            else:
                return []
