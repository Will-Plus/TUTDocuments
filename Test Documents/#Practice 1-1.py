#Practice 1-1 海伦公式计算任意三角形面积
import math
def triangle_area(a, b, c):
    # 检查三角形不等式
    if a+b<=c or a+c<=b or b+c<=a:
        return None  # 无法构成三角形
    # 计算半周长
    s=(a+b+c)/2
    # 计算面积
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

# 用户输入
print("请输入三角形的三条边长度：")
a = float(input("边a: "))
b = float(input("边b: "))
c = float(input("边c: "))

# 调用函数计算面积
result = triangle_area(a, b, c)

# 输出结果
if result is None:
    print("输入的边长无法组成三角形！")
else:
    print(f"三角形的面积为: {result:.2f}")
