#Example 8-12 输出所有水仙花数
for i in range(100,1000):
    bit=i%10
    dec=i//10%10
    hun=i//100
    if bit**3+dec**3+hun**3==i:
        print(i,)