# -*- coding:utf-8 -*-
print "����һ"
import math 
x1 = input("������x1=:")
y1 = input("������y1=:")
x2 = input("������x2=:") 
y2 = input("������y2=:") 
x3 = input("������x3=:")
y3 = input("������y3=:")
a1 = -((y2-y3)*x1-(x2-x3)*y1+x2*x3-x3*y2)/((x2-x3)*(x1-x2)*(x1-x3))
b1 = ((y2-y3)*x1**2+x2**2*y3-x3**2*y2-(x2**2-x3**2)*y1)/((x2-x3)*(x1-x2)*(x1-x2))
c1 = ((x2*y3-x3*y2)*x1**2-(x2**2-x3**2)*x1+(x2**2*x3-x2*x3**2)*y1)/((x2-x1)*(x1-x2)*(x1-x3))
print "a1=",a1,"b1=",b1,"c1=",c1
x0=input("����x0=")
y0=input("����y0=")
k = 2*a1*x0+b1
print "k=",k
xm=input("����xm=")
a2=k/2*k*(x0-xm)
b2=-k*xm/(x0-xm)
c2=-(k*x0**2-2*k*x0*xm-2*(x0-xm)*y0)/2*(x0-xm)
print "a2=",a2,"b2=",b2,"c2=",c2
y=k*(x-x0)-y0
print ��y=��,y 