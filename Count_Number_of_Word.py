,'''
Created on Feb 22, 2017

@author: Xuebin Wei
www.lbsocial.net
'''

'''
find the 10 most common words
and write the result to an excel file
'''
import xlwt        
from collections import Counter        
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
  
book = xlwt.Workbook() # create a new excel file
sheet_test = book.add_sheet('word_count') # add a new sheet
i = 0
sheet_test.write(i,0,'word') # write the header of the first column
sheet_test.write(i,1,'count') # write the header of the second column
sheet_test.write(i,2,'ratio') # write the header of the third column
    
with open('C:\\Project\\JMU\\2017 Spring\\IA241\\week11\\jmu_news.txt','r',encoding='utf-8', errors = 'ignore') as jmu_news:
     
    # convert all the word into lower cases
    # filter out stop words
    word_list = [i for i in jmu_news.read().lower().split() if i not in stop]
    word_total = word_list.__len__()
     
    count_result =  Counter(word_list)
    for result in count_result.most_common(10):
        i = i+1 
        sheet_test.write(i,0,result[0])
        sheet_test.write(i,1,result[1])
        sheet_test.write(i,2,(result[1]/word_total))
    
book.save('C:\\Project\\JMU\\2017 Spring\\IA241\\week11\\word_count.xls')
