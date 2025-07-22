"""#integer to float ,string
num=24
print(str(24))#24
print(float(24))#24.0
#to perform operations on the updated values
num=24
float_num=float(num)
print(type(float_num))#<class 'float'>
print(float_num)#24.0
print(list(34))#we can't convert int into list and tuple
"""
"""
#float to int,string
num=24.0
print(int(num))#24
print(str(num))#24.0
print(type(num))#<class 'float'>
number=int(num)
print(type(number))#<class 'int'>
"""
"""
#string to int,float,list,tuple,set
s1='123'
s2='abc12a'
print(int(s1))#123
print(float(s1))#123.0
print(list(s1))#['1', '2', '3']
print(list(s2))#['a', 'b', 'c', '1', '2', 'a']
print(tuple(s1))#('1', '2', '3')
print(tuple(s2))#('a', 'b', 'c', '1', '2', 'a')
print(set(s1))#{'1', '2', '3'}
print(set(s2))#{'b', '1', 'c', '2', 'a'}
"""
"""
#list to set,tuple,string
l=[1,2,3,'a','b',1,2]
print(set(l))#{1, 2, 3, 'a', 'b'}
print(tuple(l))#(1, 2, 3, 'a', 'b', 1, 2)
print(str(l))#[1, 2, 3, 'a', 'b', 1, 2]
s=str(l)
print(s[0])#[
print(s[-1])#]
print(s[0:5])#[1, 2
print(dict(l))#(can't convert)
"""
"""
#list of tuple to dictionary
l=[('a',1),('b',2),('c',(1,2,3))]
print(dict(l))#{'a': 1, 'b': 2, 'c': (1, 2, 3)}
"""
"""
#dictionary to list
l={'a':1,'b':2,'c':(1,2,3)}
print(list(l))#['a', 'b', 'c']
"""
"""
#tuple to list,set,string
t=(1,3,'codegnan',55)
print(list(t))#[1, 3, 'codegnan', 55]
print(set(t))#{1, 3, 55, 'codegnan'}
print(str(t))#(1, 3, 'codegnan', 55)
"""
"""
#set to list,tuple,string
s={'codegnan',1,3,55}
print(list(s))#[1, 3, 55, 'codegnan']
print(tuple(s))#(1, 3, 55, 'codegnan')
print(str(s))#(1, 3, 55, 'codegnan')
"""
"""
num=24
print(str(num)+" "+'abc')#24 abc
print(str(num)+""+'abc')#24abc
print(str(num)+'abc')#24abc
"""








































