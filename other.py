"""
班级：19计算机科学与技术2
姓名：霍烨景
学号：20190310230

"""
import os
import pandas as pd
import requests
def get_data():
    url = 'https://book.douban.com/latest'
    # headers 里面大小写均可
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'
        }
    data = requests.get(url, headers = headers)

    return data
def savepics(img_urls,titles):
    for i in range(len(img_urls)):
        img_url=img_urls[i]
        title=titles[i]
        img_data=requests.get(img_url).content#二进制内容
        with open(str(title)+'.jpg','wb') as f:
            f.write(img_data)
if __name__ == '__main__':
    if 'mypicture' not in os.listdir():
        os.mkdir('mypicture')
    os.chdir('mypicture')
    books_data=pd.read_csv('C:\\Users\\Lenovo\\PycharmProjects\\实训作业5\\result.csv')
    img_urls=books_data['img_urls']
    titles=books_data['titles']
    savepics(img_urls,titles)
