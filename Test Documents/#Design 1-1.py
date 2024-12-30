#Design 1-1 使用罗尔定理解决问题
import sympy as sp
def rolletheorem(function_input, a, b):
    #定义符号变量
    x=sp.symbols('x')
    #将输入的函数转换为符号表达式
    f=sp.sympify(function_input)
    #检查f(a)是否等于f(b)
    f_a=f.subs(x, a)
    f_b=f.subs(x, b)
    if f_a!=f_b:
        print(f"函数 f(x) 在区间 [{a}, {b}] 上不满足 f(a) = f(b)，因此罗尔定理不适用。")
        return
    #计算f(x)的导数
    f_prime=sp.diff(f, x)
    #解f'(x)=0找到 c
    critical_points=sp.solveset(f_prime, x, domain=sp.Interval(a, b))
    # 输出结果
    if critical_points:
        print(f"在区间 [{a}, {b}] 上，存在满足 f'(c)=0 的点 c: {critical_points}")
    else:
        print(f"在区间 [{a}, {b}] 上，未找到满足 f'(c)=0 的点。")
# 输入函数和区间
function_input = input("请输入函数 f(x)：")
a = float(input("请输入区间下限 a："))
b = float(input("请输入区间上限 b："))
# 调用罗尔定理验证函数
rolletheorem(function_input, a, b)