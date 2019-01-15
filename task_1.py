#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re

# Dictionary to keep the visited links
visited = {}


def crawler(url, keyword):
    """Crawler uses BeautifulSoup for crawling a webpage
    :url - the url to crawl from
    :keyword - the keyword to search for
    :return string with the """
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    answer = ''

    # For every 'a' tag with the keyword inside - we add it to the answer string.
    # For every href we check if it is in the already visited links and call the crawler again with the new link
    for text in s.findAll('a', string=re.compile('.* {0} .*'.format(keyword)), recursive=True,):
        href = text.get('href')
        answer += '\n' + str(text)
        if href not in visited:
            visited[href] = href
            crawler(href, keyword)
    return answer


# To test-run the crawler - uncomment the line below
# print(crawler('https://www.apptimist.studio/', 'website'))
