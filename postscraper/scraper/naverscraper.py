import urllib.request
from bs4 import BeautifulSoup


def getNaverBlogPost(url):
    html = urllib.request.urlopen(url).read()  # html 문서 받아오기
    soup = BeautifulSoup(html, 'html.parser')
    print(f'전달받은 url {url}')
    # iframe 벗기기.
    iframexx = soup.find('iframe')
    real_url = 'https://blog.naver.com/' + iframexx.attrs['src']

    real_html = urllib.request.urlopen(real_url).read()
    real_soup = BeautifulSoup(real_html, 'html.parser')

    title = real_soup.find(class_='se-module se-module-text se-title-text').get_text()

    print(title)

    content = real_soup.find(class_='se-main-container').find_all(class_='se-module se-module-text')

    text_list = []
    for i in content:
        print(i.get_text())
        text_list.extend(i.get_text(separator='\n').split('\n'))


    post = {}
    post['title'] = title
    post['text'] = text_list

    return post