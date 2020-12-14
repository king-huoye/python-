import csv
import xlwt
import pandas as pd

def csv_to_xlsx(csvfile):
    with open(csvfile, encoding='utf-8') as fc:
        r_csv = csv.reader(fc)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('sheet1')  # 创建一个sheet表格
        i = 0
        j = 0
        for line in r_csv:
            for v in line:
                sheet.write(i, j, v)
                j = j + 1
            i = i + 1
        workbook.save(outfile)  # 保存Excel


file = 'result.csv'  # 待转化的源文件
outfile = 'C:/Users/Lenovo/PycharmProjects/实训作业4/re.xlsx'  # 转化后的excel所处的位置与文件名

if __name__ == '__main__':
    csv_to_xlsx(file)
    print("转化完成！！！\nExcel文件所处位置：" + str(outfile))