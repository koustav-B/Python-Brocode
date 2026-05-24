#typecasting is the process of converting one data type to another data type
#there are two types of typecasting
#1. implicit typecasting
#2. explicit typecasting
#1. implicit typecasting
#in implicit typecasting, the python interpreter automatically converts one data type to another data type
a = 10
b = 20.5
c = a + b
print(c) #30.5
#2. explicit typecasting
#in explicit typecasting, the programmer manually converts one data type to another data type
x = 10
y = 20.5
z = int(x) + int(y)
print(z) #30

name="Koustav"
age=25
gpa=3.2
age+=1
cgpa=""
print(age) #26
is_student=True
type_name = type(name)
type_age = type(age)
type_gpa = type(gpa)
print(type_name) #<class 'str'>
print(type_age) #<class 'int'>
print(type_gpa) #<class 'float'>
gpa=int(gpa)
print(gpa) #3
print(float(age)) #25.0
print(bool(is_student)) #True
print(str(cgpa)) #''