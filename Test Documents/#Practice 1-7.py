#Practice 1-7  根据海伦公式，定义求三角形面积的函数，三角形三条边通过函数获取
import math
def calculate_triangle_area(a, b, c):
    """
    使用海伦公式计算三角形面积
    :param a: 三角形的第一条边
    :param b: 三角形的第二条边
    :param c: 三角形的第三条边
    :return: 三角形的面积或错误消息
    """
    # 检查三角形不等式
    if a+b<=c or a+c<=b or b+c<=a:
        return "无法组成三角形！"
    # 计算半周长
    s=(a+b+c)/2
    # 计算面积
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
# 用户输入三条边
def get_triangle_sides_and_calculate_area():
    print("请输入三角形的三条边：")
    try:
        a=float(input("边 a: "))
        b=float(input("边 b: "))
        c=float(input("边 c: "))
        # 调用面积计算函数
        result=calculate_triangle_area(a, b, c)
        if isinstance(result, str):  # 错误消息
            print(result)
        else:
            print(f"三角形的面积为: {result:.2f}")
    except ValueError:
        print("请输入有效的数字！")
# 调用函数
get_triangle_sides_and_calculate_area()