#Example 8-15计算输出斐波那契数列前n项
n=int(input("请输入n:"))
a,b=1,1
for i in range (1,n+1):
   print(a,end=' ')
   a,b=b,a+b
#请输入n:10
#1 1 2 3 5 8 13 21 34 55