
import csv
import re
import copy
import os

file = open("unittestresults.txt",'w+')
os.remove("unittestresults.txt")
monthDayArr = [31,28,31,30,31,30,31,31,30,31,30,31]
month31s = [1,3,5,7,8,10,12] ## monthlist for months with 31 days.
month30s = [4,6,9,11] ## monthlist for months with 30 days.
monthlist3 = 2 ## month with month with 28 days.

##check the year is leap year
def leapyr(year):
    leap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap= True
        else:
            leap = True
    return leap

def monthcheck(month):
        if month > 0 and month <= 12: ## If month is between 1 and 12, return True.
            return True
        else:
            return False



def daycheck(year,month,day):
    monthlist1 = [1,3,5,7,8,10,12] ## monthlist for months with 31 days.
    monthlist2 = [4,6,9,11] ## monthlist for months with 30 days.
    monthlist3 = 2 ## month with month with 28 days.
 
    for mon in monthlist1: ## iterate through monthlist1.
        if month == mon: ## Check if the parameter month equals to any month with 31 days.
            if day >=1 and day <= 31: ## If the parameter day is between 1 and 31, return True.
                return True
            else:
                return False

    for mon in monthlist2: ## iterate through the monthlist with 30 days.
        if month == mon: ## check if the parameter month equals to any month with 30 days.
            if day >= 1 and day <= 30: ## if the parameter day is between 1 and 30,return True.
                return True
            else:
                return False
    if leapyr(year) == True:
        if month == monthlist3: ## check if parameter month equals month with 28 days.
            if day >=1 and day <= 29: ## if the parameter day is between 1 and 28,return True.
                return True
            else:
                return False    
    else:
        if month == monthlist3: ## check if parameter month equals month with 28 days.
            if day >=1 and day <= 28: ## if the parameter day is between 1 and 28,return True.
                return True
            else:
                return False      
 
def yearcheck(year):
    # if len(year) >= 1 and len(year) <= 4 and year >= 1901 and year <= 2999: ## Check if year has between 1 to 4 numbers and return True.
    if year >= 1901 and year <= 2999: ## Check if year has between 1 to 4 numbers and return True.
        return True
    else:
        return False

def correctdates(year,year1,month,month1,day,day1):
  
    fyear=str(year) + str(month).zfill(2) + str(day).zfill(2)
    lyear=str(year1) + str(month1).zfill(2) + str(day1).zfill(2)
    # print("fyear,lyear",fyear,lyear)
    fyear=int(fyear)
    lyear=int(lyear)
    if lyear > fyear:
        return True
    else:
        return False
    

def findAllDaysBetweenMonths(month,month1):
    monthDayArrCpy = copy.deepcopy(monthDayArr) 
    daysinmonths = 0
    for actualmonth in range(month, month1-1):
        daysinmonths+= monthDayArrCpy[actualmonth]
    # loop between mont and month1 and add the days mentioned in above array
    return daysinmonths

def findAdditionalDays(month,year,day,day1):
    additional_days = 0
    month_days = copy.deepcopy(monthDayArr)
    if leapyr(year):
        month_days[1] =29
    start_month_days =  month_days[month-1]
    additional_days+= (day1 + (start_month_days-day))
    return additional_days

def findAllDaysInYear(month,year,start=True):
    monthDayArrCpy = copy.deepcopy(monthDayArr) 
    if leapyr(year):
        monthDayArrCpy[1]= 29
    daysinmonths = 0
    
    if start:
        for actualmonth in range(month, 12):
            daysinmonths+= monthDayArrCpy[actualmonth]
    else:
        for actualmonth in range(0, month-1):
            daysinmonths+= monthDayArrCpy[actualmonth]
        
    # loop between mont and month1 and add the days mentioned in above array
    return daysinmonths   

def findAllDaysAcrossYears(year,year1,month,month1):
    count_days_in_year = 0
    for actualYear in range(year+1,year1):
        # print (actualYear)
        if leapyr(actualYear):
            count_days_in_year+=366
        else:
            count_days_in_year+=365
    count_days_in_year+=findAllDaysInYear(month,year)
    count_days_in_year+=findAllDaysInYear(month1,year1,False)
    
    return count_days_in_year

def punc(date):
    array=[]
    for char in date:
        array.append(char)
        # print(array)
    if array[2] == "/" and array[5] == "/" and array[1]:
        for i in range(0,len(array)):
            # print(i)
            # print(array[i].isdigit())
            
            if i ==2 or i==5:
                # print("this is a number",i, array[i])
                continue
            elif array[i].isdigit():
                pass
                # print("this is a number",i, array[i])
            else:
                # print("HHH")
                return False    

        return True
    else:
        # print("asdaaaaaa")
        return False      
        
def datevalidation(date,date1):
    # print(punc(date),punc(date1))
    if punc(date) == True and punc(date1) == True:
    #get the difference year1 -year2 
        day,month,year = date.split("/") ## split the date into 3 separate variables.
        monthvalidity = monthcheck(int(month)) 
        dayvalidity = daycheck(int(year),int(month),int(day)) 
        yearvalidity = yearcheck(int(year))
        day1,month1,year1 = date1.split("/") ## split the date into 3 separate variables.
        monthvalidity1 = monthcheck(int(month1)) 
        dayvalidity1 = daycheck(int(year1),int(month1),int(day1)) 
        yearvalidity1 = yearcheck(int(year1))
        correctdates1=correctdates(int(year),int(year1),int(month),int(month1),int(day),int(day1))
    else:
        return False        
    

   
   
    # print(monthvalidity,monthvalidity1,dayvalidity,dayvalidity1,yearvalidity,yearvalidity1,correctdates1)
    if monthvalidity == True and monthvalidity1 == True and dayvalidity == True and dayvalidity1 == True and yearvalidity == True and yearvalidity1 == True  and correctdates1 ==True : ## check if all 3 variables are valid or True        
        # if monthvalidity == True and dayvalidity == True and yearvalidity == True and leapyrvalidity == True: ## check if all 3 variables are valid or True
        
        return True
    else:
        
        return False
    
def datediff(date, date1):
    day,month,year = date.split("/") ## split the date into 3 separate variables.
    day1,month1,year1 = date1.split("/") ## split the date into 3 separate variables.
    
    year = int(year)
    year1 = int(year1)
    
    month = int(month)
    month1 = int(month1)
    
    day = int (day)
    day1 = int(day1)
    
    total_days_of_year = 0
    total_days_of_month = 0
    
    
    if (year1-year) > 1:
        total_days_of_year = findAllDaysAcrossYears(year,year1,month,month1)
        total_days_of_year+=findAdditionalDays(month,year,day,day1)        
    elif (year1-year) ==0:  #Same year
        # find the days between the months
        if month1-month == 0:
            # same month find the difference of days 
            total_days_of_month+= (day1-day)
        elif month1 - month ==1:
            # 2 different months find day difference of them
            if leapyr(year) == True and month ==2:
                total_days_of_month+= (day1 + (29-day))     
            elif month ==2:
                total_days_of_month+= (day1 + (28-day))
            elif month in month31s:
                total_days_of_month+= (day1 + (31-day))    
            else:
                total_days_of_month+= (day1 + (30-day))                 
            # print("total_days_of_month",total_days_of_month)
        else:
            # find all days between month ~ month1
            total_days_of_month+=findAllDaysBetweenMonths(month,month1) #excelude month1 and month
            # add the days of month1 and month same as the above if condition
            total_days_of_month+=findAdditionalDays(month,year,day,day1) 
    elif (year1-year) ==1:
        # write a logic to find the total days of adjuscent years.
        total_days_of_month+= findAllDaysInYear(month,year)
        total_days_of_month+= findAllDaysInYear(month1,year1,False)
        total_days_of_month+=findAdditionalDays(month,year,day,day1)  
    if day==day1 and month==month1 and year==year1:
        return total_days_of_year+total_days_of_month
    return total_days_of_year+total_days_of_month-1
        


def findDateDifference(start,end):
        # print(datevalidation(start, end))
        if datevalidation(start,end) == True:
            datef=int(datediff(start,end))
            row=str(start)+','+ str(end)+','+str(datef)
            # print(type(row))
            # print(row)
            file1= open(r'unittestresults.txt', 'a')
            file1.writelines(row + "\n")
            return datef       
        else:
            datef=int(datediff(start,end))
            row=str(start)+','+ str(end)+','+str(datef)
            # print(type(row))
            # print(row)
            file1= open(r'unittestresults.txt', 'a')
            file1.writelines(row + "\n")
            return 0

# def main():
#     date = "25/02/2020"
#     date1 = "01/03/2020"
    
    
#     print(datevalidation(date,date1))
#     if  date and  date1:
#         print ("no of days between these dates are:",datediff(date, date1))
#         # print ("no of days:",datediff(date, date1))
#         return datediff(date, date1)
#     return 0



def main():
    
    # date = "29/12/2011"
    # date1 = "31/12/2021"
    while True:
        
        start=str(input("Enter the start date in dd/mm/yyyy format: ")) ## Input date in the given format.
        end=str(input("Enter the end date in dd/mm/yyyy format: ")) ## Input date in the given format.
        # start="25/02/2020"
        # end="03/03/2020"

        if not start or not end:
            print("Empty input ")
        else:

            if datevalidation(start,end) == True:
                # print (datediff(start,end))
                datef=int(datediff(start,end))
                row=str(start)+','+ str(end)+','+str(datef)
                print(row)
                return datef
                break
            else:
                print("Wrong entry please  enter dates between 01/01/1901 and 31/12/2999 and first date should be smaller than the 2nd.")
                    
        
if __name__ == '__main__':
    main()   