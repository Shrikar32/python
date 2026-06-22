#typecasting is the process of converting a variable from one data type to another. 
# In Python, you can use built-in functions like int(), float(), str(), etc., 
# to perform typecasting.
name = "shrek"
age = 25
gpa = 7.5
is_student = True
print(type(name)) 
print(type(age))
print(type(gpa))    
print(type(is_student))

gpa = int(gpa)
print(gpa)
print(type(gpa))

age = float(age)
print(age)
print(type(age))

is_student = str(is_student)
print(is_student)
print(type(is_student))
