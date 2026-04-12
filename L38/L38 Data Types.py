name = "Riya"
age = 17
is_student = True
weight = 43.2

print("original data:")

print("Name :", name)
print("Data Type of Name is", type(name))
print()

print("Age :",age)
print("Data type of age is", type(age))
print()

print("is_student :", is_student)
print("Data type of is_student is", type(is_student))
print()

print("Weight :", weight)
print("Data Type of weight is", type(weight))
print()
print()

print("After Type Casting....")
age = str(age)
print(age)

print("Data Type of age is", type(age))
print()

weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))