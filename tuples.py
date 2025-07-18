"""t=(1,2,3,'a','b','c',[4,5,6],7,1,5.2)
#immutale
t[0]=100#error becoz we can't change the values in tuple
print(t[0])#1
print(t[4])#b
print(t[-4])#[4,5,6]
print(t[2:-3:1])#(3, 'a', 'b', 'c', [4, 5, 6])
print(t[-2:6:1])#()(infinite loop so returned empty tuple)
print(t[-2:6:-1])#(1, 7)
print(t[4:100])#('b', 'c', [4, 5, 6], 7, 1, 5.2)(if there are no values for that but it is finite loop then it return s empty tuple)
"""
"""#empty list
t1=()
t2=tuple()"""

"""#tuple ith multipe values
t1=(1,2,3,'a','b')
#tuple with single value
t2=(554)


#to find the type
print(type(t1),type(t2))#<class 'tuple'> <class 'int'>"""

"""#reading inputs from tuple
t=tuple(map(int,input().split()))
print(t)
"""

"""#tuple concatination
t1=(1,2,"hi")
t2=(3,4,'Hello')
print(t1+t2)#(1, 2, 'hi', 3, 4, 'Hello')
   #[or]
t3=t1+t2
print(t3)#(1, 2, 'hi', 3, 4, 'Hello')"""

"""#tuple repetation
t1=(1,2,"hi")
print(t1*4)"""

#METHODS
"""
#index(value)
t=(1,2,3,'a','b','c',[4,5,6],7,1,5.2)
print(t.index(1))#0
#Count()
t=(1,2,3,'a','b','c',[4,5,6],7,1,5.2)
print(t.count(1))#2
"""
#BUILT IN FUNCTIONS
"""#min(),max(),sum(),len()
t=(1,2,3,5,55,44,99,100)
print(min(t))
print(max(t))
print(sum(t))
print(len(t))"""

#sorted()
#in ascending order
t=(95,3,7,1,9,3,0,5)
new_t=sorted(t,reverse=False)
print(new_t)#[0, 1, 3, 3, 5, 7, 9, 95]

#in descending order
t=(95,3,7,1,9,3,0,5)
new_t=sorted(t,reverse=True)
print(new_t)#[95, 9, 7, 5, 3, 3, 1, 0]



















