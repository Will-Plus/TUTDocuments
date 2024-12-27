#Example 8-14 计算n个连续整数阶乘之和 
n=int(input("请输入n:"))
s=0
fact=1
for i in range(1,n+1):
    fact=fact*i 
    s=s+fact 
print(s)
#请输入n:10
#4037913