# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

reload(sys)
sys.setdefaultencoding('euc-kr')

browser = webdriver.Firefox()
browser.get("https://google.com")
time.sleep(1)

f1 = open("data\\cbs_radio_20200319.text", "rt")
f2 = open("data\\cbs_radio_20200319.out", "wt")

for s in f1 :
    if "." in s :
        a = s[ len(s.split(".")[0])+1:].split("-")
        
        print a[0] + " " + a[1]
        elem1 = browser.find_element_by_name("q")
        elem1.clear()
        
        try :
            #elem1.send_keys( a[0] + u" 노래 " + a[1] + Keys.RETURN) 
            elem1.send_keys( a[0] + " song by " + a[1] + Keys.RETURN) 
        except :
            f2.write(a[0] + " - " + a[1].replace("\n","") )
            continue
        
        
        #elem2 = browser.find_element_by_name("btnk")
        #elem2.click()
        
        time.sleep(1)
        
        spans = browser.find_elements_by_xpath("//span")
        
        release_date = ""
        
        for i in range(len(spans) ) :
            #print spans[i].text
            if u"발매일" in spans[i].text : 
                print spans[i+1].text 
                release_date = spans[i+1].text 
                break
            if "release date" in spans[i].text : 
                print spans[i+1].text   
                release_date = spans[i+1].text 
                break
        else :             
            divs = browser.find_elements_by_xpath("//div//div")
            
            #print len(divs)
            
            for div in divs :
                if "Released" == div.text[:8] : 
                    print div.text 
                    release_date = div.text[9:]
                    break
                

        f2.write(a[0] + " - " + a[1].replace("\n","") + " " + release_date[:20] + "\n")
        
browser.quit()