# Python type Conversion.

# In programming its common to convert integers to float, float to string and so on..

#--> Implicit Type Conversion(automatically converts)

number_integer = 234
number_float = 1.23

sum = number_integer + number_float
print(sum)

#--> Explicit Type Conversion

float_number = 1.734
integer_number = int(float_number)

print(integer_number)
print(type(integer_number))

# Converting String to Int and Float.

a = '55'
integer_number = int(a)
float_number = float(a)

print('integer_number:', integer_number)
print('float_number:', float_number)

# Int and Float to String

a = 80
b = 80.99

str_a = str(a)
str_b = str(b)

print(str_a)
print(type(str_a))

print(str_b)
print(type(str_b))