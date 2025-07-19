s={1,2,2.5,'B','A'}
print(s)#{'B', 1, 2.5, 2, 'A'}(o/p is in zigzag manner becoz unordered)

#creating an empty set
s1={}
s2=set()
print(type(s1),type(s2))
#output:<class 'dict'> <class 'set'>

#sets not allow unhashable d.t values
s={1,2,2.5,'B','A'}
print(s[0])#type error becoz it is unhashable

#not indexbased
s={1,2,2.5,'B','A'}
print(s[2])#type error becoz it is unhashable

#allows only unique values
s={1,2,4,5,4,5,2,2.5,'B','A'}
print(s)#output:{1, 2.5, 2, 4, 5, 'A', 'B'}(doesn't allows duplicates )

#read set of integers from user
s=set(map(int,input().split()))
print(s)
#output:
1 2 3 4 5 6
{1, 2, 3, 4, 5, 6}

#read set of strings from user
s=set(map(str,input().split()))
print(s)
#output:
1 2 a e 6 9
{'2', '6', 'e', '1', '9', 'a'}
 
#read set of float from user
s=set(map(float,input().split()))
print(s)
#output:
2.5 4.5 1 2 8 
{1.0, 2.5, 2.0, 4.5, 8.0}
