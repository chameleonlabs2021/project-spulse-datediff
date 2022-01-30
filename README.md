# Download all the below files and keep it in the same directory
unittestfile.csv
unittestresults.txt
datediff_v12.py
test_datediff_ver1.2.py
test_date_prep.py
# For creating test case data run the test_date_prep.py in the below format
python3 test_date_prep.py "01/01/2021" "03/01/2021"
# Sample result below
01/12/2021
03/12/2021
Difference between dates in days:
2

# from the above result minus 1 and copy both the dates and result in this format and update the unittestfile.csv 01/01/2021,03/01/2021,1
# Once updated execute the unit test script

python3 test_datediff_ver1.2.py


         start         end  test_case_diff  difference              Test_result
0   01/01/2012  01/03/2012              58          58     Results are matching
1   25/02/2020  01/03/2020               4           4     Results are matching
2   25/02/2021  01/03/2021               3           3     Results are matching
3   25/02/2021  03/03/2021               5           5     Results are matching
4   25/02/2022  03/03/2022               5           5     Results are matching
5   01/01/2012  01/03/2013             424         424     Results are matching
6   01/01/2012  01/03/2014             789         789     Results are matching
7   01/01/2014  01/03/2012              -1          -1     Results are matching
8   01/01/1901  01/03/2014           41331       41331     Results are matching
9   01/01/2012  01/01/2012               0           0     Results are matching
10  01/01/2012  02/01/2012               0           0     Results are matching
11  01/01/1900  02/01/2012               0       40907  Result are not matching
12  01/01/1901  02/01/3000               0      401402  Result are not matching
13  25/02/1901  02/03/1901               4           4     Results are matching
14  01/12/2021  04/12/2999          357209      357209     Results are matching
# For running the original script 
python3 datediff_v12.py

Enter the start date in dd/mm/yyyy format: 01/12/2021
Enter the end date in dd/mm/yyyy format: 02/12/2021
