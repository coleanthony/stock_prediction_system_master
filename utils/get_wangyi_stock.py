# coding:utf-8
import requests
from bs4 import BeautifulSoup
import os
import time
import csv

headers={'accept':'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,*/*;q=0.8',
	'User-Agent':'Cole_Anthony/5.0 (Window NT 6.1; WOW64) AppleWebKit/537.36'
                      '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


# parameter
# shareCode/year/season : num ,
def sharesCrawl(shareCode,year,season):
    shareCodeStr = str(shareCode)
    yearStr = str(year)
    seasonStr = str(season)
    url = 'http://quotes.money.163.com/trade/lsjysj_'+shareCodeStr+'.html?year='+yearStr+'&season='+seasonStr

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')

    table = soup.findAll('table',{'class':'table_bg001'})[0]
    rows = table.findAll('tr')

    return rows[::-1]


def writeCSVWithName(shareCode,beginYear,endYear):
    shareCodeStr = str(shareCode)

    url = 'http://quotes.money.163.com/trade/lsjysj_' + shareCodeStr + '.html'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')

    name = soup.select('h1.name > a')[0].get_text()

    csvFile = open('./dataWithName/' + shareCodeStr + name + '.csv', 'wb')
    writer = csv.writer(csvFile)
    #writer.writerow(('日期','开盘价','最高价','最低价','收盘价','涨跌额','涨跌幅','成交量','成交金额','振幅','换手率'))

    try:
        for i in range(beginYear, endYear + 1):
            print (str(i) + ' is going')
            time.sleep(4)
            for j in range(1, 5):
                rows = sharesCrawl(shareCode,i,j)
                for row in rows:
                    csvRow = []
                    for cell in row.findAll('td'):
                        csvRow.append(cell.get_text().replace(',',''))
                    if csvRow != []:
                        writer.writerow(csvRow)
                time.sleep(3)
                print (str(i) + '年' + str(j)  + '季度is done')
    except:
        print ('----- 爬虫出错了！没有进入循环-----')
    finally:
        csvFile.close()

writeCSVWithName(600019,2016,2017)
