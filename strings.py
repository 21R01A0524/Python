#SLICING
n="abcde
print(n[:])#slicing of a string
print(n[1:4])
print(n[:3])
print(n[:-2])
print(n[-3:])
print(n[::2])
print(n[::-1])#reverse of a string
print(n[0:5:-1])
print(n[-5:0:-1])

#concatenation of a string
n1=n + "f"
print(n1)

#concatenation of a string with spaces using double quotes
n="sum"
m="of"
k="numbers"
print(n+" " +m+" "+k)


#concatenation of a string without spaces 
n="sum"
m="of"
k="numbers"
print(n+m+k)


#CASE CONVERSION
str1="akshAya is a student"
print(str1.lower())#every letter into small letters
print(str1.upper())#every letter into captial letters
print(str1.swapcase())#the captial is converted into small and viceversa
print(str1.title())#the first letter of each word is converted into captial
print(str1.capitalize())#only the first letter of the statement is converted into captial and all the remaining is converted into small,even any letter is captial in middle of the sentence it is converted into small

print("Hello")
print(" World!")


#STRIP:removing white spaces
str1="       I@am@a@student      "
print(str1.strip('@'))#removes both side spaces
print(str1.lstrip('@'))#removes only the spaces which are on left side
print(str1.rstrip('@'))#removes only the spaces which are in the right


#SPLIT:convert the string into list of substring as per the delimeter
str1="Akshaya is a student"
print(str1.split())#it split according to the words
#output:['Akshaya','is','a','student']
print(str1.split('a'))#the letter 'a' which is mentioned in the brackets will return the split function until the letter count
#output:['Akshaya'.'is',','student'] in this output from Akshaya word A is not seperated becoz we used small a for split but we have capital A in the sentence
print(str1.split('b')#the letter 'b' which is mentioned in the brackets will return the split function until the letter count if there no letter present then it will give same output
#output:["Akshaya is a student"]

      
#JOINS:combines all the values into single string with seperated value
l1=['I', 'am', 'a', 'student']
print(''.join(l1))#Iamastudent[no space is given]
print(' '.join(l1))#I am a student[seperated with space]
print(' @ '.join(l1))#I @ am @ a @ student[seperated with space and @ symbol]
print('_'.join(l1))#I_am_a_student[seperated with symbol '_']
print('xyz'.join(l1))#Ixyzamxyzaxyzstudent[written xyz in middle of substring] 


#FIND:returns the first position of the substring occurence or else -1
#INDEX:returns the lower position of the substring occurence or else value error
#REPLACE:old substring is replaced by new substring in all occurences
str1="I am a student"
print(str1.find('a'))#2
print(str1.find('b'))#-1
print(str1.index('a'))#2
print(str1.index('b'))#value error


#CHECKING FUNCTIONS
#isalpha()-returns true if the string contains only alphabets or else false
#isalnum()-returns true if the string contains only alphabets and numbers else false either it may be special characters or anything
#isdigit()-returns true if the string contains only numeric or else false
s1='abcd'
s2='abcd1234'
s3='1234'
s4='@1234abc'
print(s1.isalpha(),s1.isalnum(),s1.isdigit())#True True False
print(s2.isalpha(),s2.isalnum(),s2.isdigit())#False True False
print(s3.isalpha(),s3.isalnum(),s3.isdigit())#False True True
print(s4.isalpha(),s4.isalnum(),s4.isdigit())#False False False
    
#STRING COMPARISION:it compares in lexographical order by using ASCII values
s1='azcde'
s2='acde'
print(s1>s2)#True
print(s2>s1)#False


print("_".join(list('codegnan')))#c_o_d_e_g_n_a_n[string is divided into letters


#Empty String      
tr1=("  ")#empty string







