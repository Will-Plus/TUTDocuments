#Design 1-2 二、八、十六进制间的相互转换
# 用户输入数字及转换类型
print("请选择输入和输出的进制：")
print("1. 二进制（输入以 '0b' 开头）")
print("2. 八进制（输入以 '0o' 开头）")
print("3. 十进制（输入普通数字）")
print("4. 十六进制（输入以 '0x' 开头）")

# 输入数字和目标进制
input_str = input("请输入要转换的数字: ").strip()

# 判断输入类型并转换为十进制
if input_str.startswith("0b"):
    # 二进制转十进制
    num = int(input_str, 2)
elif input_str.startswith("0o"):
    # 八进制转十进制
    num = int(input_str, 8)
elif input_str.startswith("0x"):
    # 十六进制转十进制
    num = int(input_str, 16)
else:
    # 十进制输入
    num = int(input_str)

# 输出转换结果
print(f"\n{num} 的转换结果为：")
print(f"二进制: {bin(num)}")
print(f"八进制: {oct(num)}")
print(f"十进制: {num}")
print(f"十六进制: {hex(num)}")