#Example 8-18 计算并输出斐波那契数列的第n项
n=int(input("请输入n :"))
i=3
a,b=1,1
while i<=n :
    a,b=b,a+b 
    i+=1
print("数列第 %d 项是：%d"%(n,b))
#请输入n :10
#数列第 10 项是：55