#Example 8-9
y = int ( input ("请输入年份："))
if y%400==0:
   print ("%d年是闰年"%y )
else:
    if y%4==0 and y %100!=0:
        print ("%d年是闰年"%y)
    else: 
        print ("%d年不是闰年"%y)
#请输入年份：2028
#2028年是闰年
