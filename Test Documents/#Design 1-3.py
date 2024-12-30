#Design 1-3 使用洛必达法则解决问题
import sympy as sp
def lhopital_limit(f, g, x, c):
    # 计算f(x)和g(x)的导数
    f_prime=sp.diff(f, x)
    g_prime=sp.diff(g, x)
    # 计算f(x)和g(x)在x=c处的值
    f_c = f.subs(x, c)
    g_c = g.subs(x, c)
    # 判断是否是 0/0 或 ∞/∞ 类型
    if f_c==0 and g_c==0:
        print("这是一个 0/0 类型的极限，可以使用洛必达法则")
        # 计算f'(x)和g'(x)的极限
        limit_result=sp.limit(f_prime / g_prime, x, c)
        print(f"极限结果为: {limit_result}")
    elif f_c==sp.oo and g_c==sp.oo:
        print("这是一个 ∞/∞ 类型的极限，可以使用洛必达法则")
        # 计算f'(x)和g'(x)的极限
        limit_result=sp.limit(f_prime / g_prime, x, c)
        print(f"极限结果为: {limit_result}")
    else:
        print("无法应用洛必达法则，极限不是 0/0 或 ∞/∞ 类型。")
        return
# 用户输入函数和区间
x=sp.symbols('x')
f_input=input("请输入 f(x) 的函数：")
g_input=input("请输入 g(x) 的函数：")
c=float(input("请输入计算极限的点 c；"))
# 转换为符号表达式
f=sp.sympify(f_input)
g=sp.sympify(g_input)
# 调用洛必达法则计算极限
lhopital_limit(f, g, x, c)