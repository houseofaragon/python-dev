def upper_case_name(name):
    try:
        return name.upper()
    except TypeError:
        print('you must enter a name')
        

def lower_case_name(name):
    try:
        return name.lower()
    except TypeError:
        print('you must enter a name')

if __name__ == '__main__':
    names = "Karen"
    name_upper = upper_case_name(names)
    print(f"Upper case {name_upper}")
    print(f"dunder", __name__)