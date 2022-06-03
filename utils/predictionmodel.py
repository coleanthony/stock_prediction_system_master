from sklearn import svm
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, LSTM
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
from sklearn import ensemble
from sklearn import linear_model

def SVMmodel():
    '''
    :return:svm预测模型
    '''
    classifier = SVC(C=1.0, kernel='rbf', class_weight='balanced')
    c_range = np.logspace(-5, 15, 11, base=2)
    gamma_range = np.logspace(-9, 3, 13, base=2)
    # 网格搜索交叉验证的参数范围，cv=3,3折交叉
    param_grid = [{'kernel': ['rbf'], 'C': c_range, 'gamma': gamma_range}]
    grid = GridSearchCV(classifier, param_grid, cv=3, n_jobs=-1)

    regressor=svm.LinearSVR()

    return grid,regressor

def baggingmodel():
    #base DecisionTree
    c=ensemble.BaggingClassifier()
    re=ensemble.BaggingRegressor()
    return c,re

def randomforest():
    '''
    随机森林
    '''
    regressor=ensemble.RandomForestRegressor()
    model = ensemble.RandomForestClassifier(max_depth=4, n_estimators=10, min_samples_leaf=5, random_state=1)
    return model,regressor

def adaboostmodel():
    classifymodel=ensemble.AdaBoostClassifier(DecisionTreeClassifier(max_depth=2, min_samples_split=20, min_samples_leaf=5),
                         algorithm="SAMME",n_estimators=200, learning_rate=0.1)
    regressor=ensemble.AdaBoostRegressor(base_estimator=None,n_estimators=1000,learning_rate=0.3,loss='square') # 基础回归器为 LinearSVR
    return classifymodel,regressor

def xgbmodel():
    xgbcl = xgb.XGBClassifier(
        learning_rate=0.01,
        n_estimators=100,
        max_depth=3,
        min_child_weight=3,
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.8,
        objective='binary:logistic',
        eval_metric='auc',
        seed=27)

    xgbre=xgb.XGBRegressor(n_estimators=1000, learning_rate=0.05)

    return xgbcl,xgbre

def SGDmodel():
    sgdre=linear_model.SGDRegressor(max_iter=1000)
    sgdc = linear_model.SGDClassifier()
    return sgdc,sgdre

def BPmodel(X):
    model=Sequential()
    model.add(Dense(128, kernel_initializer='uniform',input_dim=X.shape[1]))  # 全连接层
    model.add(Activation('relu'))              # relu 非线性激活函数
    model.add(Dropout(0.2))                    # Dropout 将部分节点的激活值置为0，防止过拟合
    model.add(Dense(128, kernel_initializer='uniform'))  # 全连接层
    model.add(Activation('relu'))              # relu 激活函数
    model.add(Dropout(0.2))                    # Dropout 将部分节点的激活值置为0防止过拟合
    model.add(Dense(1,kernel_initializer='uniform'))                       #
    model.add(Activation('sigmoid'))
    model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    return model

def BPregr(X):
    model=Sequential()
    model.add(Dense(128, kernel_initializer='uniform',input_dim=X.shape[1]))  # 全连接层
    model.add(Activation('relu'))              # relu 非线性激活函数
    model.add(Dropout(0.2))                    # Dropout 将部分节点的激活值置为0，防止过拟合
    model.add(Dense(128, kernel_initializer='uniform'))  # 全连接层
    model.add(Activation('relu'))              # relu 激活函数
    model.add(Dropout(0.2))                    # Dropout 将部分节点的激活值置为0防止过拟合
    model.add(Dense(1,kernel_initializer='uniform'))                       #
    model.add(Activation('linear'))
    model.compile(loss='mse', optimizer='rmsprop')
    return model


def singlelstm(X):
    model = Sequential()
    model.add(LSTM(units=100, input_shape=(1, X.shape[2])))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def singlelstmre(X):
    model = Sequential()
    model.add(LSTM(units=100, input_shape=(1, X.shape[2])))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer='rmsprop')
    return model

def LSTMmodel(X):
    model = Sequential()
    model.add(LSTM(units=100, return_sequences=True,input_shape=(1,X.shape[2])))
    #model.add(Dropout(0.2))
    model.add(LSTM(units=100, return_sequences=True))
    #model.add(Dropout(0.2))
    model.add(LSTM(units=100, return_sequences=True))
    #model.add(Dropout(0.2))
    model.add(LSTM(units=100, return_sequences=False))
    #model.add(Dropout(0.2))

    model.add(Dense(100))
    model.add(Dense(output_dim=1))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
    return model

def LSTMmodelre(X):
    model = Sequential()
    model.add(LSTM(units=100, return_sequences=True,input_shape=(1,X.shape[2])))
    #model.add(Dropout(0.2))
    model.add(LSTM(units=100, return_sequences=True))
    #model.add(Dropout(0.2))
    model.add(LSTM(units=100, return_sequences=True))
    #model.add(Dropout(0.2))
    model.add(LSTM(units=100, return_sequences=False))
    #model.add(Dropout(0.2))

    model.add(Dense(100))
    model.add(Dense(output_dim=1))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer='rmsprop')
    return model

def LSTMensemble():
    '''
    LSTM与BP集成模型
    :return:
    '''

def LSTMensembleregressor():
    '''
    LSTM与BP集成模型
    :return:
    '''