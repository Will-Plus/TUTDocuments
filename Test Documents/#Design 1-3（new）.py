#Design 1-3 原码、补码、反码间的转换
# 原码转换为反码和补码的函数
def convert_code(binary_str):
    # 获取原码的符号位
    sign_bit = binary_str[0]
    
    # 处理原码的反码和补码
    if sign_bit == '0':  # 正数
        return binary_str, binary_str, binary_str
    else:  # 负数
        # 反码：符号位不变，其他位取反
        inverse_code = ''.join('1' if bit == '0' else '0' for bit in binary_str[1:])
        # 补码：反码加1
        complement_code = bin(int(inverse_code, 2) + 1)[2:].zfill(len(binary_str) - 1)
        # 返回反码和补码
        return inverse_code, complement_code

# 用户输入原码
original_code = input("请输入一个原码（以二进制表示，符号位为第一个位）：").strip()

# 输入合法性检查
if len(original_code) < 2 or not all(bit in '01' for bit in original_code):
    print("输入无效，请输入一个合法的二进制原码（如 1001101 或 010101）。")
else:
    # 获取反码和补码
    inverse_code, complement_code = convert_code(original_code)
    
    print(f"原码: {original_code}")
    print(f"反码: {inverse_code}")
    print(f"补码: {complement_code}")