import csv
import traceback
#task 3
def read_employees ():
    employees = {}
    rows=[]
    try:
        with open ('../csv/employees.csv', 'r')as file:
            reader = csv.reader(file)
            employees =[row for row in reader]
            return employees
        
    except Exception as e:
        print("An exception occured.")
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employee_name=read_employees()
if employee_name:
    get_name=[f"{row[1]+' '+row[2]}" for row in employee_name[1:]]
    print (get_name)
    name_has_e=[name for name in get_name if'e' in name.lower()]
    print(name_has_e)