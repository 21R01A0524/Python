#types:
name='akshaya'
age=21
email="akshaya@gmail.com"
print('name:',name,'age:',age,'email:',email)#name: akshaya age: 21 email: akshaya@gmail.com(old method using commas)
print('name is %s,age is %d,email is %s'%(name,age,email))#name is akshaya,age is 21,email is akshaya@gmail.com(usingmodulo operator)
print('name:%s,age:%d,email:%s'%(name,age,email))#name:akshaya,age:21,email:akshaya@gmail.com
print('name is :%s,age is :%d,email is :%s'%(name,age,email))#name is: akshaya,age is: 21,email is: akshaya@gmail.com
print(f'name is {name},age is {age},email is {email}')#name is akshaya,age is 21,email is akshaya@gmail.com(using f modulo method)

name='akshaya'
age=21.555500
email="akshaya@gmail.com"
print(f'name is {name},age is {age:.3f},email is {email}')#name is akshaya,age is 21.5555,email is akshaya@gmail.com(specifies the values)
print(f'name is {name},age is {age:3},email is {email}')#name is akshaya,age is 21.5555,email is akshaya@gmail.com
print("name is {},age is {},email is {}".format(name,age,email))#name is akshaya,age is 21.5555,email is akshaya@gmail.com(dot format method)
