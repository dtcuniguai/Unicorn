# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time

def is_date(str):
    try:
        time.strptime(str, "%Y/%m/%d")
        return True
    except:
        return False

data = {}
r = requests.get('http://www.dmm.co.jp/mono/dvd/-/detail/=/cid=h_479gne214/')

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    t = soup.find('table',class_='mg-b20').find_all('td',{'width':'100%'})
    i = 0
    for s in t :
        if s.span!=None :    # actress
            print(str(i)+' has span ' + str(s))
        elif s.a!=None:      # type....
            print(str(i)+' has url ' + str(s))
        elif is_date(s.get_text()):   # time
            data['release'] = s.get_text()
            # print(s.get_text())
        else :
            print(str(i)+' : '+str(s))
        # print(str(i)+' : '+ s.get_text())
        i+=1
