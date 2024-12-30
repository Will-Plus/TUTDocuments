#Practice 1-10 使用定积分解决问题
import sympy as sp
def calculate_definite_integral():
    #获取用户输入的函数和积分区间
    function_input=input("请输入被积函数 (例如 x**2 或 sin(x))：")
    lower_limit=float(input("请输入积分下限："))
    upper_limit=float(input("请输入积分上限："))
    #定义符号变量
    x=sp.symbols('x')
    #将输入的函数转换为符号表达式
    function=sp.sympify(function_input)
    #计算定积分
    integral_result=sp.integrate(function, (x,lower_limit,upper_limit))
    #输出结果
    print(f"定积分的结果是: {integral_result}")
#调用函数进行定积分计算
calculate_definite_integral()