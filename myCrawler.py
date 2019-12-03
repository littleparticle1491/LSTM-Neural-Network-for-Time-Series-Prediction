
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
from lxml import etree
import time

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

def myRequests(url):
    try:
        r = requests.get(url)
    except:
        try:
            r = requests.get(url)
        except Exception as e:
            print(e)
            return 'error!'
        
    time.sleep(1)
    return r

def myXpath(html, xpath):
    page_xpath = etree.HTML(html)
    try:
        scripts = page_xpath.xpath(xpath)
        if len(scripts)==1:
            result = scripts[0].text
        else:
            result = [item.text for item in scripts]
        return result
    except Exception as e:
        print(e)
        return 'error!'

def mySelenium(url):
    try:
        chrome = webdriver.Chrome(ChromeDriverManager().install())
        #chrome = webdriver.Chrome('./chromedriver')
        chrome.get(url) 
        result = chrome.page_source
        chrome.quit()  
    except Exception as e:
        print(e)
        result ='error!'
    return result

def myTable(html):
    tmp = []
    soup = BeautifulSoup(html)
    tbls = soup.find_all('tbody')
    if len(tbls) > 0:
        for tbody in tbls:
            trls = tbody.find_all('tr')
            for tr in trls:
                tdls = tr.find_all('td')
                row = [td.get_text() for td in tdls]
                tmp.append(tuple(row))
    return tmp

def Secondlink(html, classtag):
    soup = BeautifulSoup(html, features="lxml")
    a =soup.find_all('a',{'class':classtag})
    b = [(item['href'], item.get_text()) for item in a]
    return b


