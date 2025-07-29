#task2
def type_converter(type_of_output): #decorator factory
    def decorator(func): #the decorator: takes the function
        def wrapper(*args, **kwargs): #the wrapper : runs the funct with extra behavior
                    
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

y = return_int()
print(type(y).__name__) 
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!")