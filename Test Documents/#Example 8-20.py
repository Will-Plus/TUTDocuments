#Example 8-20 用辗转相除求最大公约数
m,n=eval(input("请输入 m 和 n :"))
r=m%n 
while r!=0:
    m=n 
    print(m)
    n=r 
    print(n)
    r=m%n
    print(r) 
print("最大公约数是:%d"%n)
#请输入 m 和 n :48,36
36,12,0
#最大公约数是:12