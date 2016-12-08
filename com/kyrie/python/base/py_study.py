__author__ = 'dayue'
#-*-coding:utf-8 -*-


def append_element(some_list,element):
    some_list.append(element)

data = [1,2,3]

append_element(data,4)

print data
# [1, 2, 3, 4]

#2.强类型
a = 5
print type(5)
# <type 'int'>

a = 'fuck'
print a.upper()
# FUCK

#引入模块
import firstTest as ft

ft.print_str('fuck')
# result:fuck

a =None

if a == None:
    print 'a is None'
else:
    print 'a is not None '

a = 5.6
s =str(a)
print s

#格式化字符串
template = '%.2f %s are worth $%d'
print template % (2.3333333, 'fuck you',23)
# 2.33 fuck you are worth $23



from datetime import datetime ,date,time


dt = datetime(2015,10,2,20,44,1)

print dt.day

print dt.date()
# 2015-10-02

print dt.strftime('%m/%d/%Y %H:%M')
# 10/02/2015 20:44


#3.流程控制

sequence = [1,2,None,4 ,5]

total =0
for value in sequence:
    if value is None:
        continue
    total +=value

print total
# 12

#列表推导式

strings =['certain','confident','competent','certificate']

upper = [x.upper() for x in strings if len(x) >= 9]

print upper
# ['CONFIDENT', 'COMPETENT', 'CERTIFICATE']


#enumerate
some_list =['foo','bar','bat']

mapping = dict((v,i) for i,v in enumerate(some_list))

print mapping
# {'bat': 2, 'foo': 0, 'bar': 1}


#3.5.
A = [1,2,3]
a = [1,2,3]
b = a
c =list(a)
print a is b
print a is c
# True
# False

print 2**10
# 1024

#3.7
print 3/2

print float(3)/2
# 1
# 1.5

c='''this is
a longeer
'''

print c
# this is
# a longeer

s= 'python'

print list(s)

s =r'this is \fuck spe\ \r '
print s


a =[]

if a:
    print 'is true'
else:
    print 'is false '
# is false
print bool(a)
# False

a =['a']

if not a:
    print 'is false'
else:
    print 'is true'

# is true



def add_and_mulitpy(a,b,c=None):
    result =a +b
    if c is not None:
        result = result *c
    return result

print add_and_mulitpy(2,7,3)
print add_and_mulitpy(2,7)
# 27
# 9


#3.7.5.
path ='E:\pyspace\moudle1.py'

f =open(path ,'w')
try:
    print 'execute logic'
    # write_to_file(f)
except:
    print 'failed'
else:
    print 'succeeded'
finally:
    f.close()







