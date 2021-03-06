# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res.ui'
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
from utils.predictionmodel import *
from utils.feature_engineering import *
import matplotlib.pyplot as plt
import numpy as np

class Ui_res(object):
    def __init__(self):
        self.binaryres=None
        self.regresssionres=None
        self.model=None
        self.Xtrain=None
        self.Xtrain_1=None
        self.ClassifiY=None
        self.ClassifiY_1=None
        self.RegressionY=None
        self.modelname=None

    def setupUi(self, res, Xtrain,ClassifiY,modelname):
        res.setObjectName("res")
        res.resize(800, 500)
        res.setFixedSize(res.width(), res.height())

        self.Xtrain=Xtrain
        self.ClassifiY=ClassifiY
        self.modelname=modelname

        if 'date' in self.Xtrain.columns:
            self.Xtrain.drop(['date'], axis=1, inplace=True)

        '''
        print(self.Xtrain.columns)
        print(self.modelname)
        print(ClassifiY)
        '''

        self.label = QtWidgets.QLabel(res)
        self.label.setGeometry(QtCore.QRect(100, 20, 600, 400))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(res)
        self.label_2.setGeometry(QtCore.QRect(60, 460, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(res)
        self.label_3.setGeometry(QtCore.QRect(140, 460, 72, 15))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(res)
        self.pushButton.setGeometry(QtCore.QRect(340, 450, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(res.close)

        self.retranslateUi(res)
        self.beautify(res)
        QtCore.QMetaObject.connectSlotsByName(res)
        self.run()

    def retranslateUi(self, res):
        _translate = QtCore.QCoreApplication.translate
        res.setWindowTitle(_translate("res", "Form"))
        self.label_2.setText(_translate("res", "???????????????"))
        self.label_3.setText(_translate("res", "none"))
        self.pushButton.setText(_translate("res", "??????"))

    def beautify(self,Form):
        # ??????qtawesome????????????
        Form.setWindowOpacity(0.95)
        palette = QPalette()
        path = os.path.join('source', 'timg2.jpg')
        palette.setBrush(QPalette.Background, QBrush(QPixmap(path)))
        Form.setPalette(palette)

        # icon
        iconpath = os.path.join('source', 'icon.jpg')
        Form.setWindowIcon(QIcon(iconpath))

        spin_icon3 = qtawesome.icon('fa5s.ban', color='black')
        self.pushButton.setIcon(spin_icon3)

        # ??????pushbutton??????
        self.pushButton.setStyleSheet('''QPushButton{border:none;}
                                QPushButton:hover{color:white;
                                            border:2px solid #F3F3F5;
                                            border-radius:35px;
                                            background:darkGray;}''')

    def run(self):
        self.process()
        self.predict()
        self.plot()
        self.showpic()

    def process(self):
        self.RegressionY=list(self.Xtrain['close'].values)
        self.RegressionY.pop(0)
        self.regresssionXtrain=self.Xtrain[:-1]
        self.Xtrain=scale(self.Xtrain)
        self.Xtrain_1=scale(self.regresssionXtrain)
        self.ClassifiY_1=list(self.ClassifiY)
        self.ClassifiY_1.pop(-1)

    def plot(self):
        '''
        ???????????????
        :return:
        '''
        x1=range(len(self.RegressionY))
        x2=range(len(self.regresssionres))
        plt.style.use("ggplot")
        plt.figure(figsize=(6, 4))
        y1 = self.RegressionY
        y2 = self.regresssionres
        plt.plot(x1, y1,label=['true'])
        plt.plot(x2, y2, label=['predict'])
        plt.legend()
        plt.xlabel("date")
        plt.ylabel("price")
        plt.savefig('source/result.jpg')

    def showpic(self):
        '''
        ??????
        :return:
        '''
        with open('source/result.jpg', 'rb') as f:
            self.img = f.read()
        self.imagex = QImage.fromData(self.img)
        pixmap = QPixmap.fromImage(self.imagex)
        self.label.setPixmap(QPixmap(pixmap))
        f.close()

    def predict(self):
        '''
        ??????
        '''

        if self.modelname=='SVM':
            classifymodel,regressionmodel=SVMmodel()
            classifymodel.fit(self.Xtrain_1,self.ClassifiY_1)
            regressionmodel.fit(self.Xtrain_1,self.RegressionY)
            self.binaryres=classifymodel.predict(self.Xtrain)
            self.regresssionres=regressionmodel.predict(self.Xtrain)

            if self.binaryres[-1]>=0.5:
                self.label_3.setText('??????')
            else:
                self.label_3.setText('??????')

        elif self.modelname=='random forest':
            classifymodel, regressionmodel = randomforest()
            classifymodel.fit(self.Xtrain_1, self.ClassifiY_1)
            regressionmodel.fit(self.Xtrain_1, self.RegressionY)
            self.binaryres = classifymodel.predict(self.Xtrain)
            self.regresssionres = regressionmodel.predict(self.Xtrain)

            if self.binaryres[-1] >= 0.5:
                self.label_3.setText('??????')
            else:
                self.label_3.setText('??????')

        elif self.modelname == 'XGBoost':
            classifymodel, regressionmodel = xgbmodel()
            classifymodel.fit(self.Xtrain_1, self.ClassifiY_1)
            regressionmodel.fit(self.Xtrain_1, self.RegressionY)
            self.binaryres = classifymodel.predict(self.Xtrain)
            self.regresssionres = regressionmodel.predict(self.Xtrain)

            if self.binaryres[-1] >= 0.5:
                self.label_3.setText('??????')
            else:
                self.label_3.setText('??????')

        elif self.modelname == 'SDG':
            classifymodel, regressionmodel = SGDmodel()
            classifymodel.fit(self.Xtrain_1, self.ClassifiY_1)
            regressionmodel.fit(self.Xtrain_1, self.RegressionY)
            self.binaryres = classifymodel.predict(self.Xtrain)
            self.regresssionres = regressionmodel.predict(self.Xtrain)

            if self.binaryres[-1] >= 0.5:
                self.label_3.setText('??????')
            else:
                self.label_3.setText('??????')

        elif self.modelname == 'Adaboost':
            classifymodel, regressionmodel = adaboostmodel()
            classifymodel.fit(self.Xtrain_1, self.ClassifiY_1)
            regressionmodel.fit(self.Xtrain_1, self.RegressionY)
            self.binaryres = classifymodel.predict(self.Xtrain)
            self.regresssionres = regressionmodel.predict(self.Xtrain)

            if self.binaryres[-1] >= 0.5:
                self.label_3.setText('??????')
            else:
                self.label_3.setText('??????')

        elif self.modelname == 'Bagging random forest':
            classifymodel, regressionmodel = baggingmodel()
            classifymodel.fit(self.Xtrain_1, self.ClassifiY_1)
            regressionmodel.fit(self.Xtrain_1, self.RegressionY)
            self.binaryres = classifymodel.predict(self.Xtrain)
            self.regresssionres = regressionmodel.predict(self.Xtrain)

            if self.binaryres[-1] >= 0.5:
                self.label_3.setText('??????')
            else:
                self.label_3.setText('??????')

        elif self.modelname == 'BP neural network':
            '''
            '''
            classifymodel = BPmodel(self.Xtrain_1)
            regressionmodel=BPregr(self.Xtrain_1)
            classifymodel.fit(self.Xtrain_1, np.array(self.ClassifiY_1),batch_size = 128, epochs = 100)
            regressionmodel.fit(self.Xtrain_1, np.array(self.RegressionY),batch_size = 128, epochs = 100)
            self.binaryres = classifymodel.predict(self.Xtrain)
            self.regresssionres = regressionmodel.predict(self.Xtrain)

            if self.binaryres[-1] >= 0.5:
                self.label_3.setText('??????')
            else:
                self.label_3.setText('??????')

        elif self.modelname == 'LSTM neural network':
            '''
            single lstm
            '''
            Xtrain = self.Xtrain.reshape(self.Xtrain.shape[0], 1, self.Xtrain.shape[1])
            Xtrain_1 = self.Xtrain_1.reshape(self.Xtrain_1.shape[0], 1, self.Xtrain_1.shape[1])
            classifymodel = singlelstm(Xtrain_1)
            regressionmodel = singlelstmre(Xtrain_1)
            print(Xtrain_1.shape)
            classifymodel.fit(Xtrain_1, np.array(self.ClassifiY_1), batch_size=64, nb_epoch=100,verbose=2)
            regressionmodel.fit(Xtrain_1, np.array(self.RegressionY), batch_size=32, nb_epoch=100,verbose=2)
            self.binaryres = classifymodel.predict(Xtrain)
            self.regresssionres = regressionmodel.predict(Xtrain)

            if self.binaryres[-1] >= 0.5:
                self.label_3.setText('??????')
            else:
                self.label_3.setText('??????')

        elif self.modelname=='Multilayer LSTM':
            '''
            muti lstm
            '''
            Xtrain = self.Xtrain.reshape(self.Xtrain.shape[0], 1, self.Xtrain.shape[1])
            Xtrain_1 = self.Xtrain_1.reshape(self.Xtrain_1.shape[0], 1, self.Xtrain_1.shape[1])
            classifymodel = LSTMmodel(Xtrain_1)
            regressionmodel = LSTMmodelre(Xtrain_1)
            print(Xtrain_1.shape)
            classifymodel.fit(Xtrain_1, np.array(self.ClassifiY_1), batch_size=64, nb_epoch=100, verbose=2)
            regressionmodel.fit(Xtrain_1, np.array(self.RegressionY), batch_size=32, nb_epoch=100, verbose=2)
            self.binaryres = classifymodel.predict(Xtrain)
            self.regresssionres = regressionmodel.predict(Xtrain)

            if self.binaryres[-1] >= 0.5:
                self.label_3.setText('??????')
            else:
                self.label_3.setText('??????')

        elif self.modelname == 'LSTM ensemble':
            '''
            ensemble model
            '''
            pass


