# -*- coding:utf-8 -*-
#########ѧ��������Ϣ###########
#������������
#ѧ�ţ�1403050102
#�༶��ͨ��14-1��
############��Ŀ################
#�����ʽ
import math
a=input("������a:")
b=input("������b:")
c=input("������c:")
d=b*b-4*a*c
print "d=",d
if d<0:
    print "�޽�"
else:
        x1=(-1.0*b+math.sqrt(d))/(2*a)
        x2=(-1.0*b-math.sqrt(d))/(2*a)
        print x1,x2

