#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup

text_get = requests.get('https://www.e1.ru/text/education/2023/06/19/72410909/').text
soup = BeautifulSoup(text_get, 'html.parser')

title = soup.find('h1', class_='application/ld+json').text.strip()

subtitle = soup.find('p', class_='leadParagraph_wAQ9K').text.strip()

data = {}

text_elements = soup.find_all('div', class_='uiArticleBlockText_i9h2o text-style-body-1 c-text block_fefJj')
text_data = [element.text.strip() for element in text_elements]

data['title'] = title
data['subtitle'] = subtitle
data['text'] = text_data
data.values()

