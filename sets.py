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



#METHODS
#add(ele),update(iterable),remove(ele),discard(ele),pop(),clear()
s={1,2,3,4}
print(s)#{1, 2, 3, 4}
s.add(100)
print(s)#{1, 2, 3, 100, 4}
s.update([6,8,9])
print(s)#{1, 2, 3, 100, 4, 6, 8, 9}(if the number is already present then it wont add that number)
s.remove(4)
print(s)#{1, 2, 3, 100, 6, 8, 9}
s.remove(10)
print(s)#KeyError: 10(if element is not present then it throws an key error.
s.discard(20)
print(s)#{1, 2, 3, 4}(if the element is not present then it doesnt show any error )
s.pop()
print(s)#{2, 3, 4}(it randomly pops the element)
s.clear()
print(s)#set()(clears the complete set)


#union(),intersection(),difference(),symmetricc_difference()
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.union(s2))#{1, 2, 3, 4, 5, 6}
print(s1.intersection(s2))#{3, 4}
print(s1.difference(s2))#{1, 2}
print(s2.difference(s1))#{5, 6}
print(s1.symmetric_difference(s2))#{1, 2, 5, 6}

#issubset(),issuperset(),isdisjointset()
s1={1,2,3,4,5,6}
s2={4,6}
s3={1,3,5,6,7}

print(s1.issubset(s2))#false
print(s1.issuperset(s2))#true
print(s1.isdisjoint(s2))#false
print(s2.issubset(s1))#true


#for 3 sets
print(s1.union(s2,s3))#{1, 2, 3, 4, 5, 6}
print(s1.intersection(s2,s3))#{6}
print(s1.difference(s2,s3))#{2}
print(s2.difference(s1,s3))#{}






