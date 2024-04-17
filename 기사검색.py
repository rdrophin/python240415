import requests
from bs4 import BeautifulSoup

def crawl_article_titles(url):
    # 웹페이지 요청
    response = requests.get(url)
    
    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 기사 제목 태그를 찾아서 출력
        article_titles = soup.find_all('h2', class_='article-title')  # 해당 사이트의 기사 제목 태그와 클래스를 확인하여 수정하세요.
        
        # 각 기사 제목 출력
        for title in article_titles:
            print(title.text)
    else:
        print("Error:", response.status_code)

# 크롤링할 사이트의 URL
url = "여기에_크롤링할_사이트의_URL을_입력하세요"

# 함수 호출
crawl_article_titles(url)
