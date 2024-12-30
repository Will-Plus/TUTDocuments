#Example 8-30 求满足不等式的最小正整数 m 
m=1
n=int(input("请输人n:"))
while True:
    s=0
    for i in range(m,2*m+1):
        s+= i**0.5
    if s>n:  
         break 
    m+=1
print("满足不等式的最小正整数m是：%d" %m)
#请输人n:10000
#满足不等式的最小正整数m是：407