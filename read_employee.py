import json     # JavaScript Object Notation

def read_all_employee_record():
    with open('employees_data.json', 'r') as file:
        data = json.load(file)      # json.load() takes a file object and returns the json object (key-value pair)

        for i in range(0, len(data["emp_details"])):
            if((data["emp_details"][i]["user_type"]).lower() != "admin"):
                print(data["emp_details"][i])
            else:
                continue