import name_lib

try:
    print(name_lib.upper_case_name())
except TypeError as e:
    print('error uppercasing name: ', e)
    
print(name_lib.lower_case_name("LAREN"))