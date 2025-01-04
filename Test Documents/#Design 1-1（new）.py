#Design 1-1 求出给定数范围内的所有素数
# 判断一个数是否为素数的函数
def is_prime(num):
    if num < 2:
        return False  # 0 和 1 不是素数
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # 如果能被除尽，说明不是素数
    return True

# 用户输入一个数字
n = int(input("请输入一个整数作为上限: "))

# 打印所有小于等于输入数字的素数
print(f"小于或等于 {n} 的素数有：")
for num in range(2, n+1):
    if is_prime(num):
        print(num, end=" ")