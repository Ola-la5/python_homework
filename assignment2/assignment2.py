import csv
import traceback
import os
import custom_module
from datetime import datetime
#task 2
def read_employees ():
    employees = {}
    rows=[]
    try:
        with open ('../csv/employees.csv', 'r')as file:
            reader = csv.reader(file)
            fields= next(reader)
            employees['fields']=fields
            for row in reader:
                rows.append(row)

            employees['rows'] = rows
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

employees = read_employees()
print(employees)

#task 3 
def column_index(column):
   return employees["fields"].index(column)

read_employees()
employee_id_column = column_index("employee_id")
print(f"Index of 'employee_id' column: {employee_id_column}")

#task 4
def first_name(row_num):
   column_ind = column_index("first_name")
   row = employees["rows"][row_num]
   return row[column_ind]

#task 5
def employee_find (employee_id):
    def employee_match(row):
        return int(row[employee_id_column])==employee_id
        
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#task 6
def employee_find_2(employee_id): 
    matches=list(filter(lambda row : int(row[employee_id_column])==employee_id ,employees["rows"])) 
    return matches

#task 7
def sort_by_last_name():
    index = column_index("last_name")
    employees["rows"].sort(key = lambda row:row[index])
    return employees["rows"]

sorted_l_name = sort_by_last_name()
print(sorted_l_name)

#task 8 
def employee_dict(dict_row):
    dict_result={}
    for i in range(1,len(employees["fields"])):
    
        key = employees["fields"][i]
        value = dict_row[i]
        dict_result[key]=value
    
    return dict_result
print (employee_dict(employees["rows"][2]))

#task 9 
def all_employees_dict ():
    dict_of_dict={}
    for row in employees["rows"]:
    
        employee_id=row[0]
        dict_of_dict[employee_id]=employee_dict(row)
    
    return dict_of_dict

print(all_employees_dict())

#task 10
def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value())

#task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    
set_that_secret("SHHHH!")
print(custom_module.secret)

#task 12
def read_minutes():
    def helper (path):
        input = {}
        rows= []

        with open (path, 'r')as file:
            reader = csv.reader(file)
            fields= next(reader)
            input['fields']=fields
            for row in reader:
                rows.append(tuple (row))

            input['rows'] = rows

            
            return input


    try:
        minutes1 = helper('../csv/minutes1.csv')
        minutes2 = helper('../csv/minutes2.csv')
        return minutes1, minutes2   
        
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

minutes1, minutes2 = read_minutes()
print (minutes1)
print(minutes2)

#task 13
def create_minutes_set():
    set_1 = set(minutes1['rows'])
    set_2 = set(minutes2['rows'])
    combined = set_1.union(set_2)
    return combined

minutes_set = create_minutes_set()

#task 14
def create_minutes_list():
    minutes_list = list(minutes_set)
    list_out = list(map(lambda x:(x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return list_out

minutes_list = create_minutes_list()
print(minutes_list)

#task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    minutes_converted = list(map(lambda x:(x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    
   
    with open ('./minutes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            writer.writerows(minutes_converted)

    return minutes_converted

w_list = write_sorted_list()