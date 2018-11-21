# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import re

# check input str if time
def is_date(str):
    try:
        time.strptime(str, "%Y/%m/%d")
        return True
    except:
        return False

# url parser deal data with type,work.....
def urlParser(data, url) :
    if re.search(r'maker', str(url.a)) :
        data['studio'] = url.get_text()
    elif re.search(r'keyword', str(url.a)) :
        type = ""
        for x in url.find_all('a'):
            if(re.search(r'keyword',str(x))):
                if(len(type)>0):
                    type += ','
                type += x.get_text()
        data['type'] = type

    return data

# format actress's data
def actressParser(data,actresses) :
    str = ""
    for actress in actresses :
        if(len(str)>0) :
            str += ','
        str += actress.get_text()
    data['actor'] = str
    return data


def crawler_DMM(path) :
    data = {}
    data['website'] = 'DMM.com'
    r = requests.get(path)

    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        t = soup.find('table',class_='mg-b20').find_all('td')
        data['title'] = str(soup.find('h1').get_text())
        for s in t :
            if s.span!=None :    # actress
                data = actressParser(data,s.span.find_all('a'))
            elif s.a!=None:      # type....
                data = urlParser(data,s)
            elif is_date(s.get_text()):   # time
                data['release'] = s.get_text()
            elif(re.search(r'品番：',s.get_text())):
                data['number'] = s.find_next().get_text()
            else :
                pass
        print(data)



crawler_DMM('http://www.dmm.co.jp/mono/dvd/-/detail/=/cid=118abp139/')
