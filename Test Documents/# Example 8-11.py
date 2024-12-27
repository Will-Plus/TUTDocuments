# Example 8-11 输出1~200中所有能被7整除的倍数
for i in range(1,200):
    if i%2==0 and i%7==0:
        print(i,end=' ')