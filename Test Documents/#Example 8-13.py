#Example 8-13计算n的阶乘
n=int (input("请输入n :"))
fact=1
for i in range (1,n+1):
    fact=fact*i 
print ('%d的阶乘是:%d'%(n,fact))
#请输入n :10
#10的阶乘是:3628800