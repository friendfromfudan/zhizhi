# import  csv
# import codecs
# doc_card=['12','你好']
#
# with open('/Users/youpeng/study/practice/doctor.csv', 'wb') as csvfile:
#     csvfile.write(codecs.BOM_UTF8)
#     docwriter = csv.writer(csvfile, dialect='excel')
#     docwriter.writerow(doc_card)


import csv

#csv 写入
stu1 = ['你好',26]
stu2 = ['bob',23]
#打开文件，追加a
out = open('/Users/youpeng/study/practice/doctor.csv','a', newline='')
#设定写入模式
csv_write = csv.writer(out,dialect='excel')
#写入具体内容
csv_write.writerow(stu1)
csv_write.writerow(stu2)
print ("write over")