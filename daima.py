# -*- coding:utf-8 -*-
print "方案一"
import math

#根据3点坐标计算抛物线的3个系数a,b,c
def f1(x1,y1,x2,y2,x3,y3):
	a1 = -((y2-y3)*x1-(x2-x3)*y1+x2*x3-x3*y2)/((x2-x3)*(x1-x2)*(x1-x3))
	b1 = ((y2-y3)*x1**2+x2**2*y3-x3**2*y2-(x2**2-x3**2)*y1)/((x2-x3)*(x1-x2)*(x1-x2))
	c1 = ((x2*y3-x3*y2)*x1**2-(x2**2-x3**2)*x1+(x2**2*x3-x2*x3**2)*y1)/((x2-x1)*(x1-x2)*(x1-x3))
	#函数返回3个系数的计算结果
	return a1,b1,c1

def test1():
	#输入3个点坐标
	x1 = input("请输入x1=:")
	y1 = input("请输入y1=:")
	x2 = input("请输入x2=:") 
	y2 = input("请输入y2=:") 
	x3 = input("请输入x3=:")
	y3 = input("请输入y3=:")
	#根据3点坐标计算抛物线的3个系数a,b,c
	a1,b1,c1 = f1(x1,y1,x2,y2,x3,y3)
	#打印输出计算结果
	print "a1=",a1,"b1=",b1,"c1=",c1

#根据2点坐标以及其中1点的导数来求抛物线的3个系数
def f2(a1,b1,c1, x0, y0, xmax):
	#根据公式计算a,b,c
    k = 2*a1*x0+b1
    a2 = k/(2*k*(x0-xmax))
    b2 = (-k*xmax)/(x0-xmax)
    c2 = -(k*x0**2-2*k*x0*xmax-2*(x0-xmax)*y0)/2*(x0-xmax)
    return a2,b2,c2
def test2():
    #请输入交点坐标和极大点x坐标
    a1 = input("请输入a1=:")
    b1 = input("请输入b1=:")
    c1 = input("请输入c1=:") 
    x0=input("输入x0=")
    y0=input("输入y0=")
    xmax=input("输入xmax=")
    #根据x0,y0,xm,计算a2,b2,c2
    a2,b2,c2 = f2(a1,b1,c1,x0,y0,xmax,)
    #打印出计算结果
    print "a2=",a2,"b2=",b2,"c2=",c2

#测试
test1()
test2()
    