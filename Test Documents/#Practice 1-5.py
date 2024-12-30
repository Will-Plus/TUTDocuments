#Practice 1-5 找出小于10000的最大素数
def is_prime(number):
    """判断一个数是否为素数"""
    if number<=1:
        return False
    divisor = 2
    while divisor*divisor<=number:
        if number%divisor==0:
            return False
        divisor += 1
    return True
def largest_prime_below(limit):
    """找到小于指定值的最大素数"""
    for num in range(limit-1,1,-1):  # 从 limit-1 向下查找
        if is_prime(num):
            return num
# 找出小于10000的最大素数
result=largest_prime_below(10000)
print(f"小于 10000 的最大素数是: {result}")