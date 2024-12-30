#Example 8-27
n=int(input("请输入一个大于或等于2的自然数："))
k=int(n**0.5)
for i in range(2,k+1):
    if n%i==0:
        print('%d不是素数'%n)
        break;
else:   #此处为 for 循环的 else 子句，不是 if 语句的 else 分支，注意对齐关系
    print('%d是素数'%n)