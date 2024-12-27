# Example 8-8 BMI 指数计算
h = float ( input ("请输入身高（米）:"))
w = float ( input ("请输人体重（千克）:"))
bmi = round ( w / h **2,1)
if bmi<18.5:
    lev="偏瘦"
elif 18.5<=bmi<=23.9:
    lev="正常"
elif 24<=bmi<=26.9:
    lev="偏胖"
elif 27<=bmi<=29.9:
    lev="肥胖"
else:
    lev="重度肥胖"
print ("BMI=%4.1f,体型为：%s"%(bmi,lev))
#请输入身高（米）:1.75
#请输人体重（千克）:80
#BMI=26.1,体型为：偏胖