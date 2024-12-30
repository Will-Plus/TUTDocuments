#Example 8-31 求满足等式ABC+BCC=n的A、B和C的值
n=int(input("请输入n:"))
k=0
for a in range(1,10):
    for b in range(1,10):
        for c in range(10):
            if 100*a+10*b+c+100*b+10*c+c==n and a!=b and b!=c and c!=a:
                k+=1
                print(k,":",a,b,c)
if k!=0:
    print("满足条件的解共有%d组"%k)
else:
    print("没有找到满足条件的解")
#请输入n:365   没有找到满足条件的解
#请输入n:980   1 : 1 8 0   2 : 7 2 5   满足条件的解共有2组