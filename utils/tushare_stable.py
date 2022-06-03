import tushare  as ts
import pandas as pd

def judgegetdaydata(code):
    try:
        D = ts.get_hist_data(code, ktype='D')
        res = D if D is not None else pd.DataFrame()
        if res.empty:
            return False
        else:
            return True
    except:
        return False

def judgegetweekdata(code):
    try:
        D = ts.get_hist_data(code, ktype='W')
        res = D if D is not None else pd.DataFrame()
        if res.empty:
            return False
        else:
            return True
    except:
        return False

def judgegetmonthdata(code):
    try:
        D = ts.get_hist_data(code, ktype='M')
        res = D if D is not None else pd.DataFrame()
        if res.empty:
            return False
        else:
            return True
    except:
        return False

def getday(code):
    D = ts.get_hist_data(code, ktype='D')
    return D

def getweek(code):
    D = ts.get_hist_data(code, ktype='W')
    return D

def getmonth(code):
    D = ts.get_hist_data(code, ktype='M')
    return D
