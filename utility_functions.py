import json

# function to convert string to list
def format_list(m_str):
    n = (m_str.split(','))
    res = []
    for i in n:
        res.append(i.replace(" ", ""))
    return res

# function to check employee id already exist
def check_employee_id_exist(empid):
    with open('employees_data.json', 'r') as file:
        data = json.load(file)      # json.load() takes a file object and returns the json object (key-value pair)

    emp_id_already_exist = 0    # check employee id already exist or not

    for i in range(1, len(data["emp_details"])):
        if(data["emp_details"][i]["employee_id"] == empid):
            emp_id_already_exist = 1
            break
    return emp_id_already_exist

# function to check employee user type is admin
def check_employee_usertype_is_admin(d_empid):
    with open('employees_data.json', 'r') as file:
        data = json.load(file)      # json.load() takes a file object and returns the json object (key-value pair)

    check_usertype_is_admin = 0    # check employee user type is admin

    for i in range(0, len(data["emp_details"])):
        if((data["emp_details"][i]["user_type"]).lower() == "admin" and data["emp_details"][i]["employee_id"] == d_empid):
            check_usertype_is_admin = 1
            break
    return check_usertype_is_admin

# function to check employee id is exist (to delete employee record)
def del_check_employee_id_exist(del_empid):
    with open('employees_data.json', 'r') as file:
        data = json.load(file)      # json.load() takes a file object and returns the json object (key-value pair)

    check_empid_exist = 0    # check employee id exist

    for i in range(0, len(data["emp_details"])):
        if(data["emp_details"][i]["employee_id"] == del_empid):
            check_empid_exist = 1
            break
    if(check_empid_exist == 1):
        return i        # return index of that record
    else:
        return 0