#Practice 1-4 求S=n**1+(n-1)**2+(n-2)**3+...+2**n-1+1**n（n为用户输入的一个不大于20的正整数）
def calculate_sum(n):
    if n<=0 or n>20:
        return "请输入一个不大于 20 的正整数！"
    S=0
    for i in range(1,n+1):
        S+=(n-i+1)** i
    return S
# 用户输入
n = int(input("请输入一个不大于 20 的正整数 n: "))
# 计算并输出结果
result = calculate_sum(n)
print(f"结果 S = {result}")