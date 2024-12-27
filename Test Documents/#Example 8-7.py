#Example 8-7 百分制转五档等级 
score=int( input ("请输入成绩:"))
if score>= 90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C' 
elif score>=60:
    grade='D'
else:
    grade='E'
print ('成绩等级为：%c' %grade)
#请输入成绩:85
#成绩等级为：B