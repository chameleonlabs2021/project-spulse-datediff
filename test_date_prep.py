from datetime import datetime
date_1 = '01/01/1901'
date_2 = '02/01/3000'
start = datetime.strptime(date_1, "%d/%m/%Y")
end =   datetime.strptime(date_2, "%d/%m/%Y")
# get the difference between wo dates as timedelta object
diff = end.date() - start.date() 
print('Difference between dates in days:')
print(diff.days)