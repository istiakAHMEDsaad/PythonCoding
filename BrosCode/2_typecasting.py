# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Karim"
age = 26
gpa = 3.3
is_student = True

print(f"'{name}' is: ", type(name), ",", f"'{age}' is: ", type(age), ",", f"'{gpa}' is: ", type(gpa),"\n")

int_gpa = int(gpa)
print(int_gpa)
float_age = float(age)
print(float_age)