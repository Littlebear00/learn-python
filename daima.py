# -*- coding:utf-8 -*-
print "方案一"
import math 
x1 = input("请输入x1=:")
y1 = input("请输入y1=:")
x2 = input("请输入x2=:") 
y2 = input("请输入y2=:") 
x3 = input("请输入x3=:")
y3 = input("请输入y3=:")
a1 = -((y2-y3)*x1-(x2-x3)*y1+x2*x3-x3*y2)/((x2-x3)*(x1-x2)*(x1-x3))
b1 = ((y2-y3)*x1**2+x2**2*y3-x3**2*y2-(x2**2-x3**2)*y1)/((x2-x3)*(x1-x2)*(x1-x2))
c1 = ((x2*y3-x3*y2)*x1**2-(x2**2-x3**2)*x1+(x2**2*x3-x2*x3**2)*y1)/((x2-x1)*(x1-x2)*(x1-x3))
print "a1=",a1,"b1=",b1,"c1=",c1
x0=input("输入x0=")
y0=input("输入y0=")
k = 2*a1*x0+b1
print "k=",k
xm=input("输入xm=")
a2=k/2*k*(x0-xm)
b2=-k*xm/(x0-xm)
c2=-(k*x0**2-2*k*x0*xm-2*(x0-xm)*y0)/2*(x0-xm)
print "a2=",a2,"b2=",b2,"c2=",c2
y=k*(x-x0)-y0
print “y=”,y 