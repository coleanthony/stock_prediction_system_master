#下载股票数据，存入数据库

import requests
import time
import pymysql
from sqlconnect import *
import time
import os
import json
import base64
import sqlite3
from win32crypt import CryptUnprotectData
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# 股票日线数据
# symble=股票代码
# begin=开始时间
# end=结束时间
# period=期间--day、week、month、quarter、year
# type=before，afte，normal 前除权，后，不除权
# indicator=kline，K线数据，ma-均线....kline,ma,macd,kdj,boll,rsi,wr,bias,cci,psy'

class stock_get(object):
    def __init__(self):
        self.headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                        'cache-control': 'no-cache',
                        'Connection': 'keep-alive',
                        'Host': 'stock.xueqiu.com',
                        'Referer': 'https://xueqiu.com/S',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                        'X-Requested-With': 'XMLHttpRequest'
                        }

        self.dayurl = 'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol={symbol}&begin=600000000&end={timestamp}&period=day&type=before&indicator=kline'
        self.sql=mysql_conn()

    def get_string(self,local_state):
        with open(local_state, 'r', encoding='utf-8') as f:
            s = json.load(f)['os_crypt']['encrypted_key']
        return s

    def pull_the_key(self,base64_encrypted_key):
        encrypted_key_with_header = base64.b64decode(base64_encrypted_key)
        encrypted_key = encrypted_key_with_header[5:]
        key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return key

    def decrypt_string(self,key, data):
        nonce, cipherbytes = data[3:15], data[15:]
        aesgcm = AESGCM(key)
        plainbytes = aesgcm.decrypt(nonce, cipherbytes, None)
        plaintext = plainbytes.decode('utf-8')
        return plaintext

    def getcookiefromchrome(self,host='.xueqiu.com'):
        local_state = os.environ['LOCALAPPDATA'] + r'\Google\Chrome\User Data\Local State'
        cookie_path = os.environ['LOCALAPPDATA'] + r"\Google\Chrome\User Data\Default\Cookies"

        sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host

        with sqlite3.connect(cookie_path) as conn:
            cu = conn.cursor()
            res = cu.execute(sql).fetchall()
            cu.close()
            cookies = {}
            key = self.pull_the_key(self.get_string(local_state))
            for host_key, name, encrypted_value in res:
                if encrypted_value[0:3] == b'v10':
                    cookies[name] = self.decrypt_string(key, encrypted_value)
                else:
                    cookies[name] = CryptUnprotectData(encrypted_value)[1].decode()
            return cookies

    def downloaddaykine(self,code,timestp):
        '''
        获取日k线
        :return:
        '''

        try:
            response = requests.get(self.dayurl.format(symbol=code, timestamp=timestp), headers=self.headers,cookies=self.getcookiefromchrome('.xueqiu.com'))
            res_dict = json.loads(response.text)
            print(res_dict)
            kline_json = res_dict['data']
            error_code = res_dict['error_code']
            error_description = res_dict['error_description']
            print(kline_json)
            for kline_item in kline_json['item']:
                # print(kline_item)
                data = {}
                data['symbol'] = code
                data['timestamp'] = kline_item[0] / 1000
                data['volume'] = kline_item[1]
                data['open'] = round(kline_item[2], 2)
                data['high'] = round(kline_item[3], 2)
                data['low'] = round(kline_item[4], 2)
                data['close'] = round(kline_item[5], 2)
                data['chg'] = round(kline_item[6], 2)
                data['percent'] = round(kline_item[7], 2)
                data['turnoverrate'] = round(kline_item[8], 2)  # 换手率
                data['period'] = 'day'  # 日线
                data['type'] = 'before'  # 前复权

            return True

        except:
            return False


s=stock_get()
s.downloaddaykine('SH000001')