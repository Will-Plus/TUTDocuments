#Example 8-23 判断素数
n=int(input("请输人一个自然数："))
k=int(n**0.5)
flag=True 
for i in range(2,k+1):
    if n%i==0:
        flag=False 
        break;
if flag==True:
    print('%d是素数'%n)
else:
    print('%d不是素数'%n)
#请输人一个自然数：5
#5是素数