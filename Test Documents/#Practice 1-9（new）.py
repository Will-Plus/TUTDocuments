#Practice 1-9 二进制转换为八进制、十进制、十六进制
# 定义函数进行转换
def convert_binary(binary_str):
    # 转换为十进制
    decimal = 0
    for i, bit in enumerate(reversed(binary_str)):  # 从右到左遍历
        decimal += int(bit) * (2 ** i)

    # 转换为八进制
    octal = ""
    temp_binary = binary_str.zfill((len(binary_str) + 2) // 3 * 3)  # 补足3位一组
    for i in range(0, len(temp_binary), 3):
        group = temp_binary[i:i + 3]
        octal += str(int(group, 2))

    # 转换为十六进制
    hexadecimal = ""
    temp_binary = binary_str.zfill((len(binary_str) + 3) // 4 * 4)  # 补足4位一组
    for i in range(0, len(temp_binary), 4):
        group = temp_binary[i:i + 4]
        hexadecimal += hex(int(group, 2))[2:].upper()

    return decimal, octal, hexadecimal


# 主程序
while True:
    user_input = input("请输入一个二进制数（输入 'exit' 退出程序）：")
    if user_input.lower() == "exit":
        print("程序已退出。")
        break
    if not all(bit in "01" for bit in user_input):  # 验证是否为有效二进制数
        print("请输入有效的二进制数！")
        continue

    # 调用转换函数
    decimal_result, octal_result, hexadecimal_result = convert_binary(user_input)

    # 输出结果
    print(f"二进制: {user_input}")
    print(f"十进制: {decimal_result}")
    print(f"八进制: {octal_result}")
    print(f"十六进制: {hexadecimal_result}")
    print("-" * 30)