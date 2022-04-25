'''
In parent folder powershell terminal python -m venv env

MUST INSTALL
pip install numpy
pip install pandas
pip install requests
pip install lxml
pip install bs4

'''
import numpy as np
import pandas as pd
import requests, lxml
from bs4 import BeautifulSoup
import os

headers = {
    "referer":"referer: https://www.google.com/",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }

keywords = pd.read_csv('Work-App-main\\Excel\\S_Names.csv')
collected_data = []

for query in keywords['Name']:
    html = requests.get(f'https://www.google.com/search?q={query} +Ukraine-Russia +2022', headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    
    collected_data.append({
        'Query': query
    }) 
    for result in soup.select('.tF2Cxc'):
        title = result.select_one('.DKV0Md').text
        link = result.select_one('.yuRUbf a')['href']
        #displayed_link = result.select_one('.TbwUpd.NJjxre').text
        
        try:
            snippet = result.select_one('#rso .lyLwlc').text
        except: snippet = None

        #print(f'{title}\n{link}\n{displayed_link}\n{snippet}\n')
        print(f'{title}\n{link}\n{snippet}\n')
        
        # appending all data to array as dict()
        collected_data.append({
        #'Query' : query,
        'title': title,
        'link': link,
        #'displayed link': displayed_link,
        'snippet': snippet
        })


# create dataframe and save it as .csv
df = pd.DataFrame(collected_data)
df.to_csv('Work-App-main/Excel/Queries.csv', index=False, encoding="utf-8-sig")
os.system('start EXCEL.EXE Work-App-main\\Excel\\Queries.csv')