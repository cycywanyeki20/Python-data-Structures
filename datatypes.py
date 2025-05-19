'''Data types specify the type of data that can be stored in a variable.
Python Data Types are:
1.Numeric - int, float, complex
2.String - str
3.Boolean- bool
4.sequence-list, tuple, range
5.mapping-dict
6.set-set
'''
#Numeric data types
num1=24
#Since everything in python is an object, data types are classes and variables are instances(objects) of these classes.
print(num1, 'is of type', type(num1))

num2=2.0
print(num2, 'is of type', type(num2))

num3=1+2j
print(num3, 'is of type', type(num3))

#Lists are mutable. An ordered collection of items. Lists are created using square brackets [].
Languages=['Swift', 'Java','python']
print(Languages)
print(Languages[0])
print(Languages[1])
print(Languages[2])
Languages[0]='C++' #This will not give an error because lists are mutable
print(Languages)
#Tuples. Tuples are immutable. An ordered collection of items. Tuples are created using parentheses ().Once Created, they cannot be modified.
Product=('Microsoft','Xbox', '499.99')
print(Product)
print(Product[0])
print(Product[1])
print(Product[2])

#Product[0]='Apple' #This will give an error because tuples are immutable
#print(Product)

#set. Unordered collection of items. Sets are created using curly braces {}. Sets are mutable.
student_id = {112, 114, 115, 116, 118}
print(student_id)
print(type(student_id))

#Dictionaries. Unordered collection of items. Dictionaries are created using curly braces {}. Dictionaries are mutable.
#Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is unordered, changeable and does not allow duplicates.
capital_city = {'Nepal':'Kathmadu','India':'New Delhi','Italy':'Rome'}
print(capital_city['Nepal'])
print(capital_city['Italy'])