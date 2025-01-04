#Practice 1-10 十进制转换为二进制、八进制、十六进制
# 用户输入十进制数字
decimal_number = int(input("请输入一个十进制数字: "))

# 将十进制数转换为二进制、八进制和十六进制
binary_number = bin(decimal_number)  # 转换为二进制
octal_number = oct(decimal_number)   # 转换为八进制
hexadecimal_number = hex(decimal_number)  # 转换为十六进制

# 输出转换结果
print(f"十进制数 {decimal_number} 转换为：")
print(f"二进制: {binary_number}")
print(f"八进制: {octal_number}")
print(f"十六进制: {hexadecimal_number}")