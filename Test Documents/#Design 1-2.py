#Design 1-2 使用拉格朗日中值定理解决问题
import sympy as sp
def lagrange_mean_value_theorem(function_input, a, b):
    #定义符号变量
    x=sp.symbols('x')
    #将输入的函数转换为符号表达式
    f=sp.sympify(function_input)
    #检查函数在区间[a, b]的连续性和可导性
    #SymPy 的符号计算本身会假设函数在区间内是可导的，且在区间内连续
    #计算函数的导数
    f_prime=sp.diff(f, x)
    #计算区间[a, b]上的平均变化率
    avg_rate_of_change = (f.subs(x, b) - f.subs(x, a)) / (b - a)
    #解方程f'(c)=平均变化率，找到点 c
    critical_points = sp.solveset(f_prime - avg_rate_of_change, x, domain=sp.Interval(a, b))
    #输出结果
    if critical_points:
        print(f"在区间 [{a}, {b}] 上，存在满足拉格朗日中值定理的点 c: {critical_points}")
    else:
        print(f"在区间 [{a}, {b}] 上，未找到满足条件的点。")
#输入函数和区间
function_input=input("请输入函数 f(x)：")
a=float(input("请输入区间下限 a："))
b=float(input("请输入区间上限 b："))
# 调用拉格朗日中值定理验证函数
lagrange_mean_value_theorem(function_input, a, b)