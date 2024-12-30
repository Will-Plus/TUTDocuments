#Practice 1-8 编写函数，求两个正整数m和n的最大公约数
def gcd(m, n):
    """
    使用欧几里得算法计算两个正整数m和n的最大公约数。
    :param m: 正整数 m
    :param n: 正整数 n
    :return: m和n的最大公约数
    """
    #检查输入是否为正整数，如果不符合条件则返回错误提示
    if m<=0 or n<=0:
        return "输入必须为正整数"
    #欧几里得算法：当n不为0时，计算m和n的最大公约数
    #每次迭代将m变为n，n变为m除以n的余数
    while n!= 0:  #如果n为 0，则最大公约数是m
        #更新m和n，m为n，n为m除以n的余数
        m,n=n, m%n
    #当循环结束时m即为最大公约数
    return m
# 用户输入两个正整数m和n
m = int(input("请输入第一个正整数 m: "))
n = int(input("请输入第二个正整数 n: "))
# 调用 gcd 函数计算最大公约数
result = gcd(m, n)
# 输出计算结果
print(f"{m} 和 {n} 的最大公约数是: {result}")