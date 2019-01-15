import requests
from bs4 import BeautifulSoup
import re

visited = {}


def crawler(webUrl, keyword):
    url = webUrl
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    answer = ''
    for text in s.findAll('a', string=re.compile('.* {0} .*'.format(keyword)), recursive=True,):
        href = text.get('href')
        answer += '\n' + str(text)
        if href not in visited:
            visited[href] = href
            crawler(href, keyword)
    return answer


# print(crawler('https://www.apptimist.studio/', 'website'))
