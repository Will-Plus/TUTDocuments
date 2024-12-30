#Example 8-29 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d x%d=%-4d'%(j, i, i*j),end='')
    print()