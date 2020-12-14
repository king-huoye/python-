import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter as xl
"""
班级：19计算机科学与技术2班
姓名：霍烨景
学号：20190310230
"""
url='https://book.douban.com/latest'
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}

re=requests.get(url,headers=headers)
# print(re.text)
soup=BeautifulSoup(re.text,'lxml')
#print(soup)
books_left=soup.find('ul',{'class':'cover-col-4 clearfix'})#检查元素找class
books_left=books_left.find_all('li')
books_right=soup.find('ul',{'class':'cover-col-4 pl20 clearfix'})
books_right=books_right.find_all('li')
books=list(books_right)+list(books_left)

#对每一个区块进行相同的操作，获取图片信息
img_urls=[]
titles=[]
ratings=[]
authors=[]
details=[]
for book in books:
    img_url=book.find_all('a')[0].find('img').get('src')
    img_urls.append(img_url)
    #图书标题
    book_title=book.find_all('a')[1].get_text()
    titles.append(book_title)

    #评论星级
    rating=book.find('p',{'class':"rating"}).get_text()
    rating=rating.replace("\n",'').replace(' ',' ')
    ratings.append(rating)

    ## 作者及出版信息
    author=book.find('p',{'class':'color-gray'}).get_text()
    author=author.replace('\n','').replace(' ','')
    authors.append(author)

    #图书简介
    detail=book.find_all('p')[2].get_text()
    detail=detail.replace('\n','').replace(' ','')
    details.append(detail)
print('img_urls:',img_urls)
print('titles:',titles)
print("ratings:",ratings)
print("authors:",authors)
print("details:",details)

result=pd.DataFrame()
result['img_urls']=img_urls
result['titles']=titles

result['ratings']=ratings
result['authors']=authors
result['details']=details
result.to_csv('result.csv',index=None)
