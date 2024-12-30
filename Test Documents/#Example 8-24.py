#Example 8-24 求自然数最大因子
n=int(input("请输人一个自然数："))
if n==1:
   print('1除自身外没有其他因子')
else:
     k=n//2
     while k>0:
           if n%k==0:
              break 
           k=k-1
print('%d除自身外的最大因子是:%d'%(n,k))
#请输人一个自然数：16
#16除自身外的最大因子是:8