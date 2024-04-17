import requests
from bs4 import BeautifulSoup

def crawl_naver_blog(search_keyword, page_start=1, page_end=100):
    for page in range(page_start, page_end + 1):
        # 검색할 URL
        url = f"https://search.naver.com/search.naver?where=post&query={search_keyword}&start={((page-1)*10)+1}"

        # HTTP GET 요청 보내기
        response = requests.get(url)
        if response.status_code == 200:
            # HTML 파싱
            soup = BeautifulSoup(response.text, 'html.parser')

            # 블로그 검색 결과 가져오기
            blog_results = soup.find_all('li', class_='bx')

            # 결과 출력
            for result in blog_results:
                # 블로그명과 주소
                blog_info = result.find('a', class_='sub_thumb').get('href')
                blog_name = result.find('a', class_='sub_txt').text.strip()

                # 제목
                title = result.find('a', class_='_sp_each_title').text.strip()

                # 포스팅 날짜
                date = result.find('span', class_='sub_time').text.strip()

                # 출력
                print("블로그명:", blog_name)
                print("블로그주소:", blog_info)
                print("제목:", title)
                print("포스팅 날짜:", date)
                print("="*50)
        else:
            print("HTTP 요청이 실패했습니다.")

# 사용자로부터 검색어 입력 받기
search_keyword = input("검색어를 입력하세요: ")

# 페이지 범위 설정하여 크롤링하기
crawl_naver_blog(search_keyword)
