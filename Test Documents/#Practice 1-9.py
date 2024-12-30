#Practice 1-9 使用不定积分解决问题
import sympy as sp
def calculate_indefinite_integral():
    # 获取用户输入的函数
    function_input=input("请输入被积函数 (例如 x**2 或 sin(x))：")
    # 定义符号变量
    x=sp.symbols('x')
    # 将输入的函数转换为符号表达式
    function=sp.sympify(function_input)
    # 计算不定积分
    integral_result=sp.integrate(function, x)
    # 输出结果
    print(f"不定积分的结果是: {integral_result} + C")
# 调用函数进行不定积分计算
calculate_indefinite_integral()