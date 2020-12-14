"""
班级：19计算机科学与技术2
姓名：霍烨景
学号：20190310230

"""
import os
import pandas as pd
import xlsxwriter
if 'Myxlsxdata' not in os.listdir():
    os.mkdir('Myxlsxdata')
os.chdir('Myxlsxdata')
books_data=pd.read_csv('C://Users//Lenovo//PycharmProjects//实训作业5//result.csv',usecols=['titles','authors','ratings','details'],na_values='NULL')
titles=books_data['titles']
authors=books_data['authors']
ratings=books_data['ratings']
datails=books_data['details']

workbook=xlsxwriter.Workbook('books.xlsx',{'nan_inf_to_errors': True})
worksheet=workbook.add_worksheet('豆瓣新书')
nums=len(titles)

worksheet.write(0,0,'图书封面')
worksheet.write(0,1,'图书标题')
worksheet.write(0,2,'图书作者')
worksheet.write(0,3,'图书评价')
worksheet.write(0,4,'图书细节')

worksheet.set_column('A:A',20)
worksheet.set_column('B:B',20)
worksheet.set_column('C:C',20)
worksheet.set_column('D:D',10)
worksheet.set_column('E:E',150)

for i in range(1,nums):
    worksheet.insert_image(i,0,titles[i]+'.jpg')
    worksheet.write(i,1,titles[i])
    worksheet.write(i,2,authors[i])
    #worksheet.write(i,3,ratings[i])
    worksheet.write(i,4,datails[i])
workbook.close()

