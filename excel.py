# -*- coding: utf-8 -*-
import  xdrlib ,sys
import xlrd
import xlwt
import proplanbaen


def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)


# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list


# 根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'file.xls',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数
    colnames =  table.row_values(colnameindex) #某一行数据
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list


#excel写入
def writevalue(lists):
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    scartas = ['i','j','k','l']
    scyears = [1,3,5,10]
    abcd = "a"
    sex = "y"
    years = "z"
    # 先行 再列
    for i in range(0,len(lists)):
        worksheet.write(i, 0, label = lists[i].mbaoe)
        worksheet.write(i, 1, label = lists[i].mbaof)
        worksheet.write(i, 2, label = lists[i].msex)
        worksheet.write(i, 3, label = lists[i].mage)
        worksheet.write(i, 4, label = lists[i].myears)
        worksheet.write(i, 5, label = lists[i].duration)
        # if lists[i].duration==60:
        #     abcd = 'a'
        # elif lists[i].duration==65:
        #     abcd = 'b'
        # elif lists[i].duration==70:
        #     abcd = 'c'

        #if lists[i].msex==1:
        #    sex = 'f'
        #elif lists[i].msex==2:
        #    sex = 'g'
#
        #if lists[i].myears == scyears[0]:
        #    years = scartas[0]
        #elif lists[i].myears == scyears[1]:
        #    years = scartas[1]
        #elif lists[i].myears == scyears[2]:
        #    years = scartas[2]
        #elif lists[i].myears == scyears[3]:
        #    years = scartas[3]

        #worksheet.write(i, 6, label=abcd+sex+'h'+years)

    workbook.save('Excel_Workbook.xls')
    return


def main():
   tables = excel_table_byindex()
   for row in tables:
       str_symptom = str(row).replace("u\'","\'")
       print str_symptom.decode("unicode-escape")

   tables = excel_table_byname()
   for row in tables:
       str_symptom = str(row).replace("u\'","\'")
       print str_symptom.decode("unicode-escape")

if __name__=="__main__":
    #writevalue()
    # main()
    lists = []
    obj = proplanbaen.ProplanBean(1,11,3,10000,299)
    lists.append(obj)
    obj = proplanbaen.ProplanBean(2,12,5,10000,189)
    lists.append(obj)
    writevalue(lists)