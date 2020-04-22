#-*- coding: utf-8 -*-
import sys
import re
import mechanize
import urllib2
import cookielib
from bs4 import BeautifulSoup

regex = re.compile(r'\d\d\d\d')

reload(sys)
sys.setdefaultencoding( 'utf-8' )#'euc-kr')


# mechanize 로 브라우저에 접속
        
cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.set_handle_robots(False)

br.open("https://www.cbs.co.kr/radio/pgm/board.asp?pn=list&skey=&sval=&bgrp=2&page=&bcd=00350012&pgm=111&mcd=BOARD2" )

soup = BeautifulSoup( br.response().read(), "html5lib" )

tds = soup.findAll( 'td' , attrs={ 'class' : "bd_list" }) 

for td in tds :
    #print td.text

    #if td.strong is not None :
    
    if td.a is not None :
        #print td.a["href"] #text.strip()
        
        try :
            vnum = td.a["href"].split("(")[1].split(",")[0]
            anum = td.a["href"].split(",")[1].split(")")[0]
            
            br.open( "https://www.cbs.co.kr/radio/pgm/board.asp?pn=read&skey=&sval=&anum=" + anum + "&vnum=" + vnum + "&bgrp=2&page=&bcd=00350012&pgm=111&mcd=BOARD2" ) 
        
            soup = BeautifulSoup( br.response().read(), "html5lib" )
            subject = soup.find( 'td' , attrs={ 'class' : "bd_menu_content" })          
            print subject.text.strip()
            
            matchobj = regex.search(subject.text)
            datenumber = matchobj.group()

            f1 = open ("data\\cbsradio_2020" + datenumber + ".text" , "wt" )
            
            content = soup.find( 'td' , attrs={ 'id' : "BoardContents" })  
            
            f1.write( content.text )
            
            f1.close()
        except :
            print "End of Page"
            pass
        
