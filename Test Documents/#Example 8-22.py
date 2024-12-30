#Example 8-22 计算 e 的近似值
i=1
e=1
fact=1
while(1/fact>=pow(10,-8)):
    fact*=i 
    e+=1/fact
    i+=1
print("e=",e)
#e= 2.7182818282861687