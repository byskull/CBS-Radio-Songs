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
        

    #br.open("https://www.cbs.co.kr/radio/pgm/board.asp?pn=list&skey=&sval=&bgrp=2&page=&bcd=00350012&pgm=111&mcd=BOARD2" )
    #        "https://www.cbs.co.kr/radio/pgm/board.asp?pn=read&skey=&sval=&anum=519020&vnum=" "&bgrp=2&page=&bcd=00350012&pgm=111&mcd=BOARD2"
    
'''
bd_menu_content

https://www.cbs.co.kr/radio/pgm/board.asp?pn=list&skey=&sval=&bgrp=2&page=&bcd=00350012&pgm=111&mcd=BOARD2

https://www.cbs.co.kr/radio/pgm/board.asp?pn=read&skey=&sval=&anum=519020&vnum=6891&bgrp=2&page=&bcd=00350012&pgm=111&mcd=BOARD2

https://www.cbs.co.kr/radio/pgm/board.asp?pn=read&skey=&sval=&anum=519013&vnum=6890&bgrp=2&page=&bcd=00350012&pgm=111&mcd=BOARD2


<form id="frmBoardList" name="frmBoardList" method="post" action="">
	<table border="0" cellspacing="0" cellpadding="0" width="100%">
		<tr class="bd_menu" style="height:25px" align="center">

			<td style="white-space:nowrap;width:45px" class="bd_menu">번호</td>

			<td style="white-space:nowrap;width:30px" class="bd_menu">첨부</td>

			<td style="white-space:nowrap" class="bd_menu">제목</td>

			<td style="white-space:nowrap;width:100px" class="bd_menu">글쓴이</td>

			<td style="white-space:nowrap;width:30px" class="bd_menu">조회</td>

			<td style="white-space:nowrap;width:70px" class="bd_menu">날짜</td>

		</tr>

		<tr class="bd_list" style="height:20px" align="center">

			<td style="white-space:nowrap" class="bd_list"><strong>6891</strong></td>
'''