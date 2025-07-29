import logging

#task1
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        funct_name = func.__name__
        posit_param = args if args else "none"
        keyword_param = kwargs if kwargs else "none"
        out = func(*args, **kwargs)
    
    # To write a log record:
        logger.log(logging.INFO, f"function: {funct_name}\n"
                   f"positional parameters: {posit_param}\n"
                   f"keyword parameters: {keyword_param}\n"
                   f"return: {out}\n")
        return out
    return wrapper

@logger_decorator
def hello():
   print("Hello world!")
   return None

@logger_decorator
def var_num(*args):
    return True

@logger_decorator
def no_arg(**kwargs):
    return logger_decorator

hello()
var_num(1,2,3,4)
no_arg(a=5, b=15)
