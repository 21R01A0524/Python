list1=[1,2,3,'hi','hello',25.5,5]
print(list1[0])#find the value in the mentioned index value
print(list1[-1])#find the value in the mentioned index value from backward
list1[0]=100#replacing the value and it is printed in original list
print(list1)

#To create an empty list
l=[]
print(l)


#type casting
s="Akshaya"
l=list(s)
print(type(s),type(l))
print(l)


#by default the input which is given is stored in the form string but when we mention the data type it is stored according to the data type which is mentioned.and at last the input is converted into list form
lst=list(map(int,input().split()))#string to int
print(lst)


lst=list(map(float,input().split()))#string to float
print(lst)


lst=list(map(str,input().split()))#string to string
print(lst)


#list concatenation
l1=[1,2,3,4]
l2=[4,5,6]
print(l1+l2)#output:[1, 2, 3, 4, 4, 5, 6]

l1=[1,2,3,4]
l2=[456]
print(l1+l2)#output;[[1, 2, 3, 4, 456]


#list repetation
l1=[1,2,3,4]
print(l1*4)#output:[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

l1=[12234]
print(l1*4)#output:[12234, 12234, 12234, 12234]

#List Methods
#1.append()-adds single value at the end of the list
l=[1,2,3,'a','b','c',5.5]
l.append(100)
print(l)#output:[1, 2, 3, 'a', 'b', 'c', 5.5, 100]
#2.extend()-it adds iterable values at the end of the list
l=[1,2,3,'a','b','c',5.5]
l.append([100,200])
print(l1)#output:[1, 2, 3, 'a', 'b', 'c', 5.5, [100, 200]]
#3.remove(),pop(),clear(),del
l=[1,2,3,'a','b','c',5.5]
print(l)#[1, 2, 3, 'a', 'b', 'c', 5.5]
l.remove(2)
print(l)#[1, 3, 'a', 'b', 'c', 5.5]
l=[1, 3, 'a', 'b', 'c', 5.5]
l.pop(3)
print(l)#[1, 3, 'a', 'c', 5.5]
l.clear()
print(l)#[]
l.del(2)
print(l)#[1, 3, 'c', 5.5]
#4.sort()
#min(),max(),sum()
l=[1,2,3,4,5,6,7,2,3,4]
print(max(l))#7
print(min(l))#1
print(sum(l))#37
(or)
max_value=max(l)
print(max_value)#7
min_value=min(l)
print(min_value)#1
sum_value=sum(l)
print(sum_value)#37

#reverse
l=[1,2,3,4,5,6,7,2,3,4]
l.reverse()
print(l)#[4, 3, 2, 7, 6, 5, 4, 3, 2, 1]


#sort() for ascending order
l=[1,2,3,4,5,6,7,2,3,4]
l.sort()
print(l)#[1, 2, 2, 3, 3, 4, 4, 5, 6, 7]
#for descending order
l=[1,2,3,4,5,6,7,2,3,4]
l.sort(reverse=True)
print(l)#[7, 6, 5, 4, 4, 3, 3, 2, 2, 1]


#sorted()-sorts the particular list and returns the new list
l=[200,4,1,5,8,2,0]
new_list=sorted(l)
print(new_list)#output:[0, 1, 2, 4, 5, 8, 200]

#count(value)
l=[200,5,4,1,5,8,2,0]
print(l.count(5))#2
l=[200,5,4,1,5,8,2,0]
print(l.count(100))#0

#index(value)
l=[200,5,4,1,5,8,2,0]
print(l.index(5))#1
l=[200,5,4,1,5,8,2,0]
print(l.count(100))#0

#len()
l=[200,5,4,1,5,8,2,0]
print(len(l))#8
    [or]
l=[200,5,4,1,5,8,2,0]
length=len(l)
print(length)#8

#insert()
l=[200,5,4,1,5,8,2,0]
l.insert(5,300)
print(l)#[200, 5, 4, 1, 5, 300, 8, 2, 0]

#index
l=[200,5,4,1,5,8,2,0] #2
print(l.index(50))#value error






