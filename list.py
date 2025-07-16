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


