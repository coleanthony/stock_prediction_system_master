import time
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from snownlp import SnowNLP
import urllib

headers={'accept':'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,*/*;q=0.8',
	'User-Agent':'Cole_Anthony/5.0 (Window NT 6.1; WOW64) AppleWebKit/537.36'
                      '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

def date_change(date):
    timeArray = time.strptime(date, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def gettext(dates,name):
    pos=[]
    for date in dates:
        print('downloading ',date)
        timestr=date_change(date)
        article=[]
        url = 'https://www.baidu.com/s?wd='+ name+ '&gpc=stf={},{}'.format(str(timestr),str(timestr))+'&pn=0'
        web_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        tagh3 = soup.find_all('h3')
        for h3 in tagh3:
            try:
                href = h3.find("a")
                we=href.attrs['href']
                a = Article(we)
                a.download()
                a.parse()
                article.append(a.text)
            except:
                pass
        if len(article)==0:
            pos.append(0.5)
            continue
        else:
            s=''
            for i in range(len(article)):
                s+=article[i]
            if len(s)==0:
                pos.append(0.5)
            else:
                m = SnowNLP(s)
                sentiment=m.sentiments
                pos.append(sentiment)
    return pos

'''
dates=['2018-02-10','2019-02-01','2020-9-10']
name='上证指数'
gettext(dates,name)
'''









