import pandas as pd
import talib
import numpy as np
from sklearn.preprocessing import StandardScaler

def basicfeature(data):
    '''
    自动预测特征构建
    :param data: pd.DateFrame
    '''
    data['H-L'] = data['high'] - data['low']
    data['O-C'] = data['close'] - data['open']
    #data['5day MA'] = data['close'].shift(1).rolling(window=30).mean()
    data['30day MA'] = data['close'].shift(1).rolling(window=30).mean()
    #data['15day MA'] = data['close'].shift(1).rolling(window=30).mean()
    data['Std_dev'] = data['close'].rolling(5).std()
    data['RSI'] = talib.RSI(data['close'].values, timeperiod=9)
    data['Williams %R'] = talib.WILLR(data['high'].values, data['low'].values, data['close'].values, 7)
    data['MACD'], data['MACDsignal'], data['MACDhist'] = talib.MACD(np.array(data['close']), fastperiod=6,                                                                 slowperiod=12, signalperiod=9)
    data['EMA12'] = talib.EMA(np.array(data['close']), timeperiod=6)
    data['EMA26'] = talib.EMA(np.array(data['close']), timeperiod=12)

def makey(data):
    '''
    创建特征y
    :param data: pd.DataFrame
    :return: none
    '''
    y = np.where(data['close'].shift(-1) > data['close'], 1, 0)
    return y

def scale(data):
    sc = StandardScaler()
    X = sc.fit_transform(data)
    return X

def BBAMDS_bands5(data):
    '''
    BBANDS - Bollinger Bands
    布林线指标，即BOLL指标，其英文全称是“Bollinger Bands”，布林线(BOLL)由约翰·布林先生创造，其利用统计原理，求出股价的标准差及其信赖
    区间，从而确定股价的波动范围及未来走势，利用波带显示股价的安全高低价位，因而也被称为布林带。其上下限范围不固定，随股价的滚动而变化。布林
    指标和麦克指标MIKE一样同属路径指标，股价波动在上限和下限的区间之内，这条带状区的宽窄，随着股价波动幅度的大小而变化，股价涨跌幅度加大时，
    带状区变宽，涨跌幅度狭小盘整时，带状区则变窄
    '''
    data['upperband_5'], data['middleband_5'], data['lowerband_5'] = talib.BBANDS(data['close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)

def BBAMDS_bands15(data):
    '''
    BBANDS - Bollinger Bands
    布林线指标，即BOLL指标，其英文全称是“Bollinger Bands”，布林线(BOLL)由约翰·布林先生创造，其利用统计原理，求出股价的标准差及其信赖
    区间，从而确定股价的波动范围及未来走势，利用波带显示股价的安全高低价位，因而也被称为布林带。其上下限范围不固定，随股价的滚动而变化。布林
    指标和麦克指标MIKE一样同属路径指标，股价波动在上限和下限的区间之内，这条带状区的宽窄，随着股价波动幅度的大小而变化，股价涨跌幅度加大时，
    带状区变宽，涨跌幅度狭小盘整时，带状区则变窄
    '''
    data['upperband_15'], data['middleband_15'], data['lowerband_15'] = talib.BBANDS(data['close'], timeperiod=15, nbdevup=2, nbdevdn=2, matype=0)

def BBAMDS_bands30(data):
    '''
    BBANDS - Bollinger Bands
    布林线指标，即BOLL指标，其英文全称是“Bollinger Bands”，布林线(BOLL)由约翰·布林先生创造，其利用统计原理，求出股价的标准差及其信赖
    区间，从而确定股价的波动范围及未来走势，利用波带显示股价的安全高低价位，因而也被称为布林带。其上下限范围不固定，随股价的滚动而变化。布林
    指标和麦克指标MIKE一样同属路径指标，股价波动在上限和下限的区间之内，这条带状区的宽窄，随着股价波动幅度的大小而变化，股价涨跌幅度加大时，
    带状区变宽，涨跌幅度狭小盘整时，带状区则变窄
    '''
    data['upperband_30'], data['middleband_30'], data['lowerband_30'] = talib.BBANDS(data['close'], timeperiod=30, nbdevup=2, nbdevdn=2, matype=0)

def DEMA_7(data):
    '''
    DEMA - Double Exponential Moving Average
    双指数移动平均线(DEMA)是由Patrick Mulloy发明的，目的是为了减少延迟和增加反应能力。这种快速移动平均线允许交易者快速发现趋势逆转，从
    而更好地进入新形成的趋势。该指标显然是基于指数移动平均线(EMA)但它更贴近价格。它的计算和使用有点像船体移动均线(HMA)。它帮助交易者发现当
    前的趋势，并经常与其他信号和分析技术结合使用。
    :param data:
    '''
    data['dema7'] = talib.DEMA(data['close'], timeperiod=7)

def DEMA_15(data):
    '''
    DEMA - Double Exponential Moving Average
    双指数移动平均线(DEMA)是由Patrick Mulloy发明的，目的是为了减少延迟和增加反应能力。这种快速移动平均线允许交易者快速发现趋势逆转，从
    而更好地进入新形成的趋势。该指标显然是基于指数移动平均线(EMA)但它更贴近价格。它的计算和使用有点像船体移动均线(HMA)。它帮助交易者发现当
    前的趋势，并经常与其他信号和分析技术结合使用。
    :param data:
    '''
    data['dema15'] = talib.DEMA(data['close'], timeperiod=15)

def DEMA_30(data):
    '''
    DEMA - Double Exponential Moving Average
    双指数移动平均线(DEMA)是由Patrick Mulloy发明的，目的是为了减少延迟和增加反应能力。这种快速移动平均线允许交易者快速发现趋势逆转，从
    而更好地进入新形成的趋势。该指标显然是基于指数移动平均线(EMA)但它更贴近价格。它的计算和使用有点像船体移动均线(HMA)。它帮助交易者发现当
    前的趋势，并经常与其他信号和分析技术结合使用。
    :param data:
    '''
    data['dema30'] = talib.DEMA(data['close'], timeperiod=30)

def EMA12(data):
    '''
    EMA - Exponential Moving Average
    EMA即指数平均数指标（ Exponential Moving Average， EXPMA或EMA），也是一种趋向类指标。其构造原理是：对收盘价进行算术平均，用于
    判断价格未来走势的变动趋势。与MACD指标、DMA指标相比，EMA指标由于其计算公式中着重考虑了当天价格（当期）行情的权重，决定了其作为一类趋
    势分析指标，在使用中克服了MACD指标对于价格走势的滞后性缺陷，同时，也在一定程度上消除了DMA指标在某些时候对于价格走势所产生的信号提前性
    ，是一个非常有效的分析指标。
    :param data:
    :return:
    '''
    data['ema12'] = talib.EMA(data['close'], timeperiod=12)

def EMA30(data):
    '''
    EMA - Exponential Moving Average
    EMA即指数平均数指标（ Exponential Moving Average， EXPMA或EMA），也是一种趋向类指标。其构造原理是：对收盘价进行算术平均，用于
    判断价格未来走势的变动趋势。与MACD指标、DMA指标相比，EMA指标由于其计算公式中着重考虑了当天价格（当期）行情的权重，决定了其作为一类趋
    势分析指标，在使用中克服了MACD指标对于价格走势的滞后性缺陷，同时，也在一定程度上消除了DMA指标在某些时候对于价格走势所产生的信号提前性
    ，是一个非常有效的分析指标。
    :param data:
    :return:
    '''
    data['ema30'] = talib.EMA(data['close'], timeperiod=30)

def HTTRENDLINE(data):
    '''
    HT_TRENDLINE - Hilbert Transform - Instantaneous Trendline
    希尔伯特顺时变换是一种趋向类指标，其构造原理是仍然对价格收盘价进行算数平均，并根据计算结果来进行分析。用来判断变动趋势。
    :param data:
    :return:
    '''
    data['HT_TRENDLINE'] = talib.HT_TRENDLINE(data['close'])

def kama7(data):
    '''
    KAMA - Kaufman Adaptive Moving Average
    KAMA隶属于MA(Moving Average，移动平均)大类，使用CrossOver（上穿，下穿）或者平滑曲线的斜率来生成交易信号。KAMA“聪明”之处在于，
    能根据市场趋势变化速度自主调节，避免震荡行情中的虚假信号，同时消除长期趋势中的滞后。在牛市和熊市中自适应均线紧随指数向上或向下变化，而
    在市场处于横盘震荡时期，其变化明显减慢，从而减少因噪声产生的交易成本。
    :param data:
    :return:
    '''
    data['kama7'] = talib.KAMA(data['close'], timeperiod=7)

def kama20(data):
    '''
    KAMA - Kaufman Adaptive Moving Average
    KAMA隶属于MA(Moving Average，移动平均)大类，使用CrossOver（上穿，下穿）或者平滑曲线的斜率来生成交易信号。KAMA“聪明”之处在于，
    能根据市场趋势变化速度自主调节，避免震荡行情中的虚假信号，同时消除长期趋势中的滞后。在牛市和熊市中自适应均线紧随指数向上或向下变化，而
    在市场处于横盘震荡时期，其变化明显减慢，从而减少因噪声产生的交易成本。
    :param data:
    :return:
    '''
    data['kama20'] = talib.KAMA(data['close'], timeperiod=20)

def kama30(data):
    '''
    KAMA - Kaufman Adaptive Moving Average
    KAMA隶属于MA(Moving Average，移动平均)大类，使用CrossOver（上穿，下穿）或者平滑曲线的斜率来生成交易信号。KAMA“聪明”之处在于，
    能根据市场趋势变化速度自主调节，避免震荡行情中的虚假信号，同时消除长期趋势中的滞后。在牛市和熊市中自适应均线紧随指数向上或向下变化，而
    在市场处于横盘震荡时期，其变化明显减慢，从而减少因噪声产生的交易成本。
    :param data:
    :return:
    '''
    data['kama30'] = talib.KAMA(data['close'], timeperiod=30)

def MA5(data):
    '''
    MA指标是英文(Moving average)的简写，叫移动平均线指标。移动平均线（MA）具有趋势的特性，它比较平稳，不像日K线会起起落落地震荡。
    越长期的移动平均线，越能表现稳定的特性。不轻易向上向下，必须等股价趋势的真正明朗。移动平均线说到底是一种趋势追踪工具，便于识别趋势
    已经终结或者反转，新的趋势是否正在形成。
    :param data:
    :return:
    '''
    data['ma5'] = talib.MA(data['close'], timeperiod=5, matype=0)

def MA10(data):
    '''
    MA指标是英文(Moving average)的简写，叫移动平均线指标。移动平均线（MA）具有趋势的特性，它比较平稳，不像日K线会起起落落地震荡。
    越长期的移动平均线，越能表现稳定的特性。不轻易向上向下，必须等股价趋势的真正明朗。移动平均线说到底是一种趋势追踪工具，便于识别趋势
    已经终结或者反转，新的趋势是否正在形成。
    :param data:
    :return:
    '''
    data['ma10'] = talib.MA(data['close'], timeperiod=10, matype=0)

def MA20(data):
    '''
    MA指标是英文(Moving average)的简写，叫移动平均线指标。移动平均线（MA）具有趋势的特性，它比较平稳，不像日K线会起起落落地震荡。
    越长期的移动平均线，越能表现稳定的特性。不轻易向上向下，必须等股价趋势的真正明朗。移动平均线说到底是一种趋势追踪工具，便于识别趋势
    已经终结或者反转，新的趋势是否正在形成。
    :param data:
    :return:
    '''
    data['ma20'] = talib.MA(data['close'], timeperiod=20, matype=0)

def MA30(data):
    '''
    MA指标是英文(Moving average)的简写，叫移动平均线指标。移动平均线（MA）具有趋势的特性，它比较平稳，不像日K线会起起落落地震荡。
    越长期的移动平均线，越能表现稳定的特性。不轻易向上向下，必须等股价趋势的真正明朗。移动平均线说到底是一种趋势追踪工具，便于识别趋势
    已经终结或者反转，新的趋势是否正在形成。
    :param data:
    :return:
    '''
    data['ma30'] = talib.MA(data['close'], timeperiod=30, matype=0)

def MAMA0(data):
    '''
    MAMA - MESA Adaptive Moving  Average
    MAMA指标是由约翰·埃勒斯发明的，交易者可以将其理解为一种比较特殊的均线指标。MAMA指标由两条类似移动平均线的指标线组成的，
    一条是快速线，另一条是慢速线，因此，快慢两条线的交叉可以产生交易信号。
    :param data:
    :return:
    '''
    #data['mama'], data['fama'] = talib.MAMA(data['close'], fastlimit=12, slowlimit=26)

def minpoint14(data):
    '''
    MIDPOINT - MidPoint over period
    :param data:
    :return:
    '''
    data['minpoint14'] = talib.MIDPOINT(data['close'], timeperiod=14)

def midprice14(data):
    '''
    MIDPRICE - Midpoint Price over period
    '''
    data['minprice14'] = talib.MIDPRICE(data['high'], data['low'], timeperiod=14)

def SAR0(data):
    '''
    SAR - Parabolic SAR
    SAR指标又叫抛物线指标或停损转向操作点指标，其全称叫“Stop and Reverse，缩写SAR”，是由美国技术分析大师
    威尔斯-威尔德（Wells Wilder）所创造的，是一种简单易学、比较准确的中短期技术分析工具。
    :param data:
    :return:
    '''
    data['sar'] = talib.SAR(data['high'], data['low'], acceleration=0, maximum=0)

def sarext(data):
    '''
    SAREXT - Parabolic SAR - Extended
    '''
    data['sarext'] = talib.SAREXT(data['high'], data['low'], startvalue=0, offsetonreverse=0, accelerationinitlong=0,
                  accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0,
                  accelerationmaxshort=0)

def SMA7(data):
    '''
    SMA - Simple Moving Average
    SMA(X,N,M)，求X的N日移动平均，M为权重。算法：若Y=SMA(X,N,M) 则 Y=(M*X+(N-M)*Y')/N，其中Y'表示上一周期Y值，N必须大于M。
    '''
    data['sma7'] = talib.SMA(data['close'], timeperiod=7)

def SMA15(data):
    '''
    SMA - Simple Moving Average
    SMA(X,N,M)，求X的N日移动平均，M为权重。算法：若Y=SMA(X,N,M) 则 Y=(M*X+(N-M)*Y')/N，其中Y'表示上一周期Y值，N必须大于M。
    '''
    data['sma15'] = talib.SMA(data['close'], timeperiod=15)

def SMA30(data):
    '''
    SMA - Simple Moving Average
    SMA(X,N,M)，求X的N日移动平均，M为权重。算法：若Y=SMA(X,N,M) 则 Y=(M*X+(N-M)*Y')/N，其中Y'表示上一周期Y值，N必须大于M。
    '''
    data['sma30'] = talib.SMA(data['close'], timeperiod=30)

def T35(data):
    '''
    T3 - Triple Exponential Moving Average(T3)
    '''
    data['t3_5'] = talib.T3(data['close'], timeperiod=5, vfactor=0)

def TEMA5(data):
    '''
    TEMA - Triple Exponential Moving Average
    三指数移动平均线(TEMA)是受欢迎的指数移动平均线的强化版。TEMA更快对市场变动采取行动及有更大的回应。它原本是由Patrick Mulloy构思的。
    '''
    data['tema5'] = talib.TEMA(data['close'], timeperiod=5)

def TEMA15(data):
    '''
    TEMA - Triple Exponential Moving Average
    三指数移动平均线(TEMA)是受欢迎的指数移动平均线的强化版。TEMA更快对市场变动采取行动及有更大的回应。它原本是由Patrick Mulloy构思的。
    '''
    data['tema15'] = talib.TEMA(data['close'], timeperiod=15)

def TEMA30(data):
    '''
    TEMA - Triple Exponential Moving Average
    三指数移动平均线(TEMA)是受欢迎的指数移动平均线的强化版。TEMA更快对市场变动采取行动及有更大的回应。它原本是由Patrick Mulloy构思的。
    '''
    data['tema30'] = talib.TEMA(data['close'], timeperiod=30)

def trima30(data):
    '''
    TRIMA - Triangular Moving Average
    '''
    data['trima'] = talib.TRIMA(data['close'], timeperiod=30)

def WMA30(data):
    '''
    WMA - Weighted Moving  Average
    '''
    data['wma30'] = talib.WMA(data['close'], timeperiod=30)

def ADX14(data):
    '''
    ADX - Average Directional Movement Index
    使用DMI(ADX)指标其实很简单，就是观察+DI、-DI和ADX这三条线的变化，信号
    很清晰，也很可靠。它是判断顶部和底部的重要指标，准确率较高，适合做中长线的
    汇友使用;DMI(ADX)中长线预测比较准确。短线出错率较高，建议大家结合RSI及S
    AR应用比较好一点。
    :param data:
    :return:
    '''
    data['ADX14'] = talib.ADX(data['high'], data['low'], data['close'], timeperiod=14)

def ADXR14(data):
    '''
    ADXR - Average Directional Movement Index Rating
    '''
    data['adxr14'] = talib.ADXR(data['high'], data['low'], data['close'], timeperiod=14)

def APO12(data):
    '''
    APO - Absolute Price Oscillator
    绝对价格振荡器
    :param data:
    :return:
    '''
    data['apo1226'] = talib.APO(data['close'], fastperiod=12, slowperiod=26, matype=0)

def Aroon14(data):
    '''
    AROON - Aroon
    阿隆指标是由图莎尔·钱德（Tushar Chande）发明的，该指标是通过计算自价格达到近期最高值和最低值以来所经过的期间数，阿隆指标帮助你预测
    价格趋势到趋势区域（或者反过来，从趋势区域到趋势）的变化。
    '''
    data['aroondown14'], data['aroonup14'] = talib.AROON(data['high'], data['low'], timeperiod=14)

def Aroonosc14(data):
    '''
    AROONOSC - Aroon Oscillator
    '''
    data['aroonosc14'] = talib.AROONOSC(data['high'], data['low'], timeperiod=14)

def BOP0(data):
    '''
    BOP - Balance Of Power
    (推动力平衡) 是一款振荡器,
    '''
    data['bop'] = talib.BOP(data['open'], data['high'], data['low'], data['close'])

def CCI14(data):
    '''
    CCI - Commodity Channel Index
    顺势指标又叫CCI指标，CCI指标是美国股市技术分析 家唐纳德·蓝伯特(Donald Lambert)于20世纪80年代提出的，专门测量股价、
    外汇或者贵金属交易是否已超出常态分布范围。属于超买超卖类指标中较特殊的一种。波动于正无穷大和负无穷大之间。但是，又不需要
    以0为中轴线，这一点也和波动于正无穷大和负无穷大的指标不同。
    :param data:
    :return:
    '''
    data['CCI14'] = talib.CCI(data['high'], data['low'], data['close'], timeperiod=14)

def CMO14(data):
    '''
    CMO - Chande Momentum Oscillator
    钱德动量摆动指标（Chande Momentum Osciliator，简称CMO）是由图莎尔·钱德（Tushar S.Chande）发明的，
    与其他动量指标摆动指标如相对强弱指标（RSI）和随机指标（KDJ）不同，钱德动量指标在计算公式的分子中采用上涨日
    和下跌日的数据。 CMO指标是寻找极度超买和极度超卖的条件。
    '''
    data['cmo14'] = talib.CMO(data['close'], timeperiod=14)

def DX14(data):
    '''
    DX - Directional Movement Index
    动向指标DX
    '''
    data['dx14'] = talib.DX(data['high'], data['low'], data['close'], timeperiod=14)

def MACD0(data):
    '''
    MACD - Moving Average= Convergence / Divergence
    MACD称为异同移动平均线，是从双指数移动平均线发展而来的，由快的指数移动平均线（EMA12）减去慢的指数移动平均线（EMA26）得到快线DIF，
    再用2×（快线DIF-DIF的9日加权移动均线DEA）得到MACD柱。MACD的意义和双移动平均线基本相同，即由快、慢均线的离散、聚合表征当前的多空
    状态和股价可能的发展变化趋势，但阅读起来更方便。MACD的变化代表着市场趋势的变化，不同K线级别的MACD代表当前级别周期中的买卖趋势。
    '''
    data['macd'], data['macdsignal'], data['macdhist'] = talib.MACD(data['close'], fastperiod=12, slowperiod=26, signalperiod=9)

def MACTEXT0(data):
    #MACDEXT - MACD with controllable MA type
    data['macdext'], data['macdsignalext'], data['macdhistext'] = talib.MACDEXT(data['close'], fastperiod=12, fastmatype=0, slowperiod=26,
                                         slowmatype=0, signalperiod=9, signalmatype=0)

def MACDFIX0(data):
    #MACDFIX - Moving Average Convergence / Divergence Fix 12 / 26
    data['macds9'], data['macdsignals9'], data['macdhists9'] = talib.MACDFIX(data['close'], signalperiod=9)

def MFI14(data):
    '''
    MFI - Money Flow Index
    MFI资金流量指标，它是在RSI指标基础上修改而bai来的，它是价和量的结合，它就是成交量的RSI指标。它也同样具有超买超卖的作用。
    '''
    data['mfi14'] = talib.MFI(data['high'], data['low'], data['close'], data['volume'], timeperiod=14)

def MINUS_DI14(data):
    #MINUS_DI - Minus Directional Indicator
    data['minus_di14'] = talib.MINUS_DI(data['high'], data['low'], data['close'], timeperiod=14)

def MINUS_DM14(data):
    #MINUS_DM - Minus Directional Movement
    data['minusdm14'] = talib.MINUS_DM(data['high'], data['low'], timeperiod=14)

def MOM30(data):
    '''
    一般股民，经常将Momentum视为超买超卖指标，而忽略其在“速度”方面的表现。事实上，将Momentum解释成“速度线”，更符合其实际的作用。
    理论上，一波健全的股价趋势，其上涨或下跌的过程，应该维持着一定的行进速度。如果行进的速度逐渐减缓，股价很容易转变成整理的格局，甚
    至于反转。因此，观察股价的速度感，对于股价多空力道的判定，有很大的帮助。
    MOM - Momentum
    :param data:
    :return:
    '''
    data['mom30'] = talib.MOM(data['close'], timeperiod=30)

def MOM20(data):
    '''
    一般股民，经常将Momentum视为超买超卖指标，而忽略其在“速度”方面的表现。事实上，将Momentum解释成“速度线”，更符合其实际的作用。
    理论上，一波健全的股价趋势，其上涨或下跌的过程，应该维持着一定的行进速度。如果行进的速度逐渐减缓，股价很容易转变成整理的格局，甚
    至于反转。因此，观察股价的速度感，对于股价多空力道的判定，有很大的帮助。
    MOM - Momentum
    :param data:
    :return:
    '''
    data['mom20'] = talib.MOM(data['close'], timeperiod=20)

def MOM10(data):
    '''
    一般股民，经常将Momentum视为超买超卖指标，而忽略其在“速度”方面的表现。事实上，将Momentum解释成“速度线”，更符合其实际的作用。
    理论上，一波健全的股价趋势，其上涨或下跌的过程，应该维持着一定的行进速度。如果行进的速度逐渐减缓，股价很容易转变成整理的格局，甚
    至于反转。因此，观察股价的速度感，对于股价多空力道的判定，有很大的帮助。
    MOM - Momentum
    :param data:
    :return:
    '''
    data['mom10'] = talib.MOM(data['close'], timeperiod=10)

def RSI14(data):
    '''
    RSI - Relative Strength Index
    RSI最早被用于期货交易中，后来人们发现用该指标来指导股票市场投资效果也十分不错，并对该指标的特点不断进行归纳和总结。
    现在，RSI已经成为被投资者应用最广泛的技术指标之一。投资的一般原理认为，投资者的买卖行为是各种因素综合结果的反映，
    行情的变化最终取决于供求关系，而RSI指标正是根据供求平衡的原理，通过测量某一个期间内股价上涨总幅度占股价变化总幅度
    平均值的百分比，来评估多空力量的强弱程度，进而提示具体操作的。RSI的应用法则表面上比较复杂，包括了交叉、数值、形态
    和背离等多方面的判断原则。
    :param data:
    :return:
    '''
    data['rsi14'] = talib.RSI(data['close'], timeperiod=14)

def AD0(data):
    #AD - Chaikin A / D Line
    data['adline'] = talib.AD(data['high'], data['low'], data['close'], data['volume'])

def ADOSC0(data):
    #ADOSC - Chaikin A / D Oscillator
    data['adosc'] = talib.ADOSC(data['high'], data['low'], data['close'], data['volume'], fastperiod=3, slowperiod=10)

def OBV0(data):
    '''
    OBV - On Balance Volume
    OBV [1]  的英文全称是：On Balance Volume，是由美国的投资分析家Joe Granville所创。该指标通过统计成交量变动的趋势来推测股价趋势。
    OBV以“N”字型为波动单位，并且由许许多多“N”型波构成了OBV的曲线图，对一浪高于一浪的“N”型波，称其为“上升潮”（UP TIDE），至于上升潮中
    的下跌回落则称为“跌潮”（DOWN FIELD）。能量潮是将成交量数量化，制成趋势线，配合股价趋势线，从价格的变动及成交量的增减关系，推测市场气
    氛。其主要理论基础是市场价格的变化必须有成交量的配合，股价的波动与成交量的扩大或萎缩有密切的关连。通常股价上升所需的成交量总是较大；下跌
    时，则成交量可能放大，也可能较小。价格升降而成交量不相应升降，则市场价格的变动难以为继。
    :param data:
    :return:
    '''
    data['obv'] = talib.OBV(data['close'], data['volume'])

def ATR14(data):
    '''
    ATR - Average True Range
    :param data:
    :return:
    '''
    data['atr14'] = talib.ATR(data['high'], data['low'], data['close'], timeperiod=14)

def NATR14(data):
    '''
    NATR - Normalized Average True Range
    :param data:
    :return:
    '''
    data['natr14'] = talib.NATR(data['high'], data['low'], data['close'], timeperiod=14)

def TRANGE0(data):
    '''
    TRANGE - True Range 真实波动幅度
    :param data:
    :return:
    '''
    data['trange'] = talib.TRANGE(data['high'], data['low'], data['close'])

def avgprice(data):
    #AVGPRICE - Average Price
    data['avg'] = talib.AVGPRICE(data['open'], data['high'], data['low'], data['close'])

def MEDPRICE0(data):
    data['medprice'] = talib.MEDPRICE(data['high'], data['low'])

def TYPPRICE0(data):
    #- Typical Price
    data['typprice'] = talib.TYPPRICE(data['high'], data['low'], data['close'])

def WCLPRICE0(data):
    #- Weighted  Close Price
    data['wclprice'] = talib.WCLPRICE(data['high'], data['low'], data['close'])

def HT_DCPERIOD(data):
    #- Hilbert Transform - Dominant Cycle  Period
    data['htdcperiod'] = talib.HT_DCPERIOD(data['close'])

def HT_DCPHASE(data):
    #- Hilbert Transform - Dominant Cycle Phase
    data['htdcphase'] = talib.HT_DCPHASE(data['close'])

def HT_PHASOR(data):
    #- Hilbert Transform - Phasor Components
    data['inphase'], data['quadrature'] = talib.HT_PHASOR(data['close'])

def HT_SINE(data):
    #- Hilbert Transform - SineWave
    data['sine'], data['leadsine'] = talib.HT_SINE(data['close'])

def HT_TRENDMODE(data):
    #- Hilbert Transform - Trend vs Cycle Mode
    data['httrdmode'] = talib.HT_TRENDMODE(data['close'])

def BETA0(data):
    #- Beta
    '''
    beta值，是一种风险指数，用来衡量个别股票或股票基金相对于整个股市的价格波动情况。β值越高，意味
    着股票相对于业绩评价基准的波动性越大，反之亦然。 当β=1时，表示该股票的收益和风险与大盘指数收益
    和风险一致；当β>1时，表示该股票收益和风险均大于大盘指数的收益和风险。
    :param data:
    :return:
    '''
    data['beta5'] = talib.BETA(data['high'], data['low'], timeperiod=5)

def CORREL30(data):
    #CORREL - Pearson‘s Correlation Coefficient (r)
    data['correl30'] = talib.CORREL(data['high'], data['low'], timeperiod=30)

def LINEARREG14(data):
    #- Linear Regression
    data['linerreg14'] = talib.LINEARREG(data['close'], timeperiod=14)

def LINEARREG_ANGLE14(data):
    #- Linear Regression Angle
    data['linearrref14'] = talib.LINEARREG_ANGLE(data['close'], timeperiod=14)

def LINEARREG_INTERCEPT14(data):
    #- Linear Regression Intercept
    data['LINEARREG_INTERCEPT14'] = talib.LINEARREG_INTERCEPT(data['close'], timeperiod=14)

def LINEARREG_SLOPE14(data):
    #LINEARREG_SLOPE - Linear Regression Slope
    data['LINEARREG_SLOPE14'] = talib.LINEARREG_SLOPE(data['close'], timeperiod=14)

def stddev5(data):
    '''
    STDDEV - Standard Deviation
    Standard Deviation，StdDev，标准偏差指标，目的是用来衡量价格的波动性，该指标是用一条曲线来表示其波动性的，
    如果标准差大，就说明价格波动性大；如果标准差小，就说明价格波动性小，该指标把标准差和平均值用来衡量市场的波动性。
    标准偏差是测量变动的统计测算法。它通常不用做独立的指标而与其他指标配合使用。
    '''
    data['STDDEV5'] = talib.STDDEV(data['close'], timeperiod=5, nbdev=1)

def TSF14(data):
    '''
    TSF - Time Series Forecast
     时间持续猜测
    :param data:
    :return:
    '''

    data['tsf14'] = talib.TSF(data['close'], timeperiod=14)

def VAR5(data):
    '''
    VAR - Variance
    协方差（Covariance）在概率论和统计学中用于衡量两个变量的总体误差。而方差是协方差的一种特殊情况，即当两个变量是相同的情况。
    协方差表示的是两个变量的总体的误差，这与只表示一个变量误差的方差不同。 如果两个变量的变化趋势一致，也就是说如果其中一个大于自身的期望值
    ，另外一个也大于自身的期望值，那么两个变量之间的协方差就是正值。 如果两个变量的变化趋势相反，即其中一个大于自身的期望值，另外一个却小于自
    身的期望值，那么两个变量之间的协方差就是负值。
    :param data:
    :return:
    '''

    data['var5'] = talib.VAR(data['close'], timeperiod=5, nbdev=1)

def acos(data):
    #ACOS - Vector Trigonometric ACos
    data['acos'] = talib.ACOS(data['close'])

def asin(data):
    #ASIN - Vector Trigonometric ASin
    data['asin'] = talib.ASIN(data['close'])

def atan(data):
    #ATAN - Vector Trigonometric ATan
    data['atan'] = talib.ATAN(data['close'])

def vecceil(data):
    #CEIL - Vector Ceil
    data['ceil'] = talib.CEIL(data['close'])

def cos(data):
    #COS - Vector Trigonometric  Cos
    data['cos'] = talib.COS(data['close'])

def cosh(data):
    #COSH - Vector Trigonometric Cosh
    data['cosh'] = talib.COSH(data['close'])

def vexp(data):
    #EXP - Vector Arithmetic Exp
    data['exp'] = talib.EXP(data['close'])

def vectorfloor(data):
    #FLOOR - Vector Floor
    data['floor'] = talib.FLOOR(data['close'])

def LN0(data):
    #LN - Vector Log Natural
    data['LN'] =talib. LN(data['close'])

def log10(data):
    #LOG10 - Vector  Log10
    data['log10'] = talib.LOG10(data['close'])

def sin(data):
    #SIN - Vector Trigonometric Sin
    data['SIN'] = talib.SIN(data['close'])

def sinh(data):
    #SINH - Vector Trigonometric Sinh
    data['SINH'] = talib.SINH(data['close'])

def sqrt(data):
    #SQRT - Vector Square Root
    data['SQRT'] = talib.SQRT(data['close'])

def tan(data):
    #TAN - Vector Trigonometric Tan
    data['TAN'] = talib.TAN(data['close'])

def tanh(data):
    #TANH - Vector Trigonometric Tanh
    data['TANH'] = talib.TANH(data['close'])

def add(data):
    #ADD - Vector Arithmetic Add
    data['ADD'] = talib.ADD(data['high'], data['low'])

def div(data):
    #DIV - Vector Arithmetic Div
    data['DIV'] = talib.DIV(data['high'], data['low'])

def highest(data):
    #MAX - Highest value  over  a specified period
    data['MAX30'] = talib.MAX(data['close'], timeperiod=30)

def maxindex(data):
    #MAXINDEX - Index of value over a specified period
    data['maxindex30'] = talib.MAXINDEX(data['close'], timeperiod=30)

def lowest(data):
    #MIN - Lowest value  over  a  specified period
    data['MIN30'] = talib.MIN(data['close'], timeperiod=30)

def minindex(data):
    #MININDEX - Index of  lowest value over a specified  period
    data['Minindex30'] = talib.MININDEX(data['close'] ,timeperiod=30)

def minmax(data):
    #MINMAX - Lowest and highest values over  a specified period
    data['min30'], data['max30'] = talib.MINMAX(data['close'], timeperiod=30)

def minmaxindex(data):
    #MINMAXINDEX - Indexes of lowest and highest  values over a specified period
    data['minidx30'],data['maxidx30'] = talib.MINMAXINDEX(data['high'], timeperiod=30)

def multy(data):
    #MULT - Vector Arithmetic Mult
    data['mult'] = talib.MULT(data['high'], data['low'])

def subtra(data):
    '''
    SUB - Vector Arithmetic Substraction
    '''
    data['sub'] = talib.SUB(data['high'], data['low'])

def summation30(data):
    '''
    SUM - Summation
    '''
    data['sum30'] = talib.SUM(data['close'], timeperiod=30)
