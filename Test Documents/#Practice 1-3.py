#Practice 1-3 判断一个数是否为素数
def is_prime(number):
    if number <= 1:
        return False  # 小于等于 1 的数不是素数
    # 从 2 开始逐一检查是否能整除
    divisor = 2
    while divisor * divisor <= number:  # 只需检查到平方根
        if number % divisor == 0:
            return False  # 能被整除，不是素数
        divisor += 1
    return True  # 没有找到因数，说明是素数
# 用户输入
num = int(input("请输入一个正整数: "))
# 调用函数并输出结果
if is_prime(num):
    print(f"{num} 是素数。")
else:
    print(f"{num} 不是素数。")