# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의유머 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
#<td class="subject">
#<a href="/board/view.php?table=bestofbest&amp;no=474681&amp;s_no=474681&amp;page=1" target="_top">시골 병원 경고문</a>
#<span class="list_memo_count_span"> [16]</span>  
        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        title = item.find("a").text.strip() 
                        #print(title)
                        if (re.search('한국', title)):
                                print(title.strip())
                                #print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
