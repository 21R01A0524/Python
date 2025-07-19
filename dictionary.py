d={1:'a','A':2,6:4,(1,2):4,5:[1,2,(3,4),5]}
print(d.keys())#dict_keys([1, 'A', 6, (1, 2), 5])
print(d.values())#dict_values(['a', 2, 4, 4, [1, 2, (3, 4), 5]])
print(d[0])#key error becoz the key is not present
print(d[1])#a"""

#empty dictionary
d={}
d1=dict()



#accessing the values in dictionary-the keys which are in the dict only can be accessed if there is no key in the dict then it will give key error 
d={1:'a','A':2,6:4,(1,2):4,5:[1,2,(3,4),5]}
print(d[0])#key error becoz the key is not present
print(d[1])#a


#METHODS
#keys(),items(),values()
#d={'language':'python','version':'3.13.5','level':'high'}
keys=d.keys()
values=d.values()
items=d.items()
print(type(keys))
print(type(values))
print(type(items))
print(keys)
print(values)
print(items)
#output:
<class 'dict_keys'>
<class 'dict_values'>
<class 'dict_items'>
dict_keys(['language', 'version', 'level'])
dict_values(['python', '3.13.5', 'high'])
dict_items([('language', 'python'), ('version', '3.13.5'), ('level', 'high')])
print(d.keys())


#to convert it into list
items=d.items()
print(type(items))
print(items)
items_list=list(items)
print(type(items_list))
print(items_list)
a,b=items_list[1]
print(a,b)
#output:
<class 'dict_items'>
dict_items([('language', 'python'), ('version', '3.13.5'), ('level', 'high')])
<class 'list'>
[('language', 'python'), ('version', '3.13.5'), ('level', 'high')]
version 3.13.5

#pop(),popitem()
val=d.pop('version')
print(val)
print(d)
#output:
3.13.5
{'language': 'python', 'level': 'high'}


val=d.popitem()
print(val)
print(d)
#output:
('level', 'high')
{'language': 'python', 'version': '3.13.5'}

#value access and updating the values(if there is no key in the list and if we add any new key value pair then it will add at the last and it is performed without using methods)
print(d['language'])
d['A']=1
d['language']='java'
print(d)
#output:
python
{'language': 'java', 'version': '3.13.5', 'level': 'high', 'A': 1}


#with using methods
#get(key,default):return the value of a key or else default value
#update(dictionary):updates the dict with new items .
val=d.get('version','key is not in dict')
print(val)#3.13.5
val=d.get('A','key is not in dict')
print(val)#key is not in dict(this default value may be anything,if u did't write default then it will none in o/p screen)

#update()
d1={'language':'python','version':'3.13.5'}
d2={'language':'java','level':'high'}
d1.update(d2)
print(d1)
print(d2)
#output:
{'language': 'java', 'version': '3.13.5', 'level': 'high'}
{'language': 'java', 'level': 'high'}
d2.update(d1)
print(d1)
print(d2)
#output:
{'language': 'java', 'version': '3.13.5', 'level': 'high'}
{'language': 'java', 'level': 'high', 'version': '3.13.5'}

#clear():removes all items from dictionary
d1={'language':'python','version':'3.13.5'}
d1.clear()
print(d1)#{}

#to access the value by using indexing wrt keys
d={'a':[1,2,3,4],3:[40,5,6,7]}
print(d[3][0])#40(initializing and using should be same in both.)
d={'a':[1,2,3,4],'3':[40,5,6,7]}
print(d['3'][0])#40











