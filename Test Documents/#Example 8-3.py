#Example 8-3 改进的计算球体表面积和体积
from math import *
r=float(input("请输入半径："))
if r>0:
    s=round(4*pi*r*r,2)
    v=round(4/3*pi*pow(r,3),2)
    print("球表面积为：",s)
    print("球体积为：",v)