
from datediff_v12 import findDateDifference
import pandas as pd    
import numpy as np 
import pandasql as psql
from datetime import datetime 
from pandas.io.sql import to_sql, read_sql
import csv
from datetime import date
import re

         
testfile="unittestfile.csv"

def numOfDays(date1, date2):
    return (date2-date1).days
     
with open(testfile, mode='r') as csv_file:
    this_csv_reader = csv.reader(csv_file, skipinitialspace=False,delimiter=',', quoting=csv.QUOTE_NONE)
    # print "{0}".format(csv_file.readline().split())
    
    for line in  this_csv_reader:
          findDateDifference(line[0],line[1])

          
testfile="unittestfile.csv"
resultfile="unittestresults.txt"
df_result= pd.read_csv(resultfile)
df_result = pd.read_csv(resultfile, sep=',', header=None)
df_result.columns = ['start', 'end', 'difference']
df= pd.read_csv(testfile)
pd.set_option('display.max_colwidth', 1000)
df = pd.read_csv(testfile, sep=',', header=None)
df.columns = ['start', 'end', 'difference']
df_result.drop_duplicates()
df.drop_duplicates()
          

df_test = """ SELECT distinct * FROM df""" 
df_result1 = """ SELECT distinct * FROM df_result""" 

df2="""select a.start,a.end,a.difference as test_case,b.difference as original, CASE
    WHEN a.difference=b.difference THEN 'Results are matching'
    ELSE 'Result are not matching'
END AS Test_result from df a inner join df_result b on (a.start=b.start and a.end=b.end)"""
print(psql.sqldf(df2))