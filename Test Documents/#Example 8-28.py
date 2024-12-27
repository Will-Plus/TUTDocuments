#Example 8-28 求100以内的所有素数
import math
print(2,end='')
for n in range(3,100,2):
    k=int(n**0.5)
    for i in range (2,k+1):
        if n%i==0:
            break;
else:                         # 内层for循环的else子句，注意缩进及对齐关系
    print(n,end='')