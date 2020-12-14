import requests
from bs4 import BeautifulSoup
url='https://www.taobao.com/'
headers={
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
data=requests.get(url,headers=headers)
print(data.text)
data_latest=BeautifulSoup(data.text,'lxml')

