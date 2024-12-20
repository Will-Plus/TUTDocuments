#Example 8-2 计算球体表面积和体积
import math
r=float(input ("请输入半径："))
s=round(4*math.pi*r*r,2)
v=round(4/3*math.pi*pow(r,3),2)
print("球表面积为：",s)
print("球体积为：",v)