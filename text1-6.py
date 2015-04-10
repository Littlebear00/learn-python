# -*- coding:utf-8 -*-
#########学生基本信息###########
#姓名：陈晓军
#学号：1403050102
#班级：通风14-1班
############题目################
#求根公式
import math
a=input("请输入a:")
b=input("请输入b:")
c=input("请输入c:")
d=b*b-4*a*c
print "d=",d
if d<0:
    print "无解"
else:
        x1=(-1.0*b+math.sqrt(d))/(2*a)
        x2=(-1.0*b-math.sqrt(d))/(2*a)
        print x1,x2

