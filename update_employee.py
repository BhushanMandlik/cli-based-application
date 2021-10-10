import json     # JavaScript Object Notation
import utility_functions
import logging

def update_emp_record():
    up_emp_id = input("Enter Employee id to update record: ")

    up_usertype_is_admin = utility_functions.check_employee_usertype_is_admin(int(up_emp_id))

    if(up_usertype_is_admin == 1):
        print("Admin data not editable")
        print()
    else:
        up_employee_id_exist = utility_functions.del_check_employee_id_exist(int(up_emp_id))    # it holds index of record
        # print(up_employee_id_exist)

        if(up_employee_id_exist == 0):
            print("Employee id not exist")
        else:
            # print("You can update")
            print()
            print("*** Welcome to update section ***")
            print("Note: please press enter key to skip\n")

            name = input("Update employee name: ")
            user_type = input("Update employee user type: ")
            project_name = input("Update employee project name: ")
            year_of_exp = input("Update employee year of exp: ")
            skill_sets = input("Update employee skill sets: ")
            joining_date = input("Update employee joining date (DD/MM/YYYY): ")
            DOB = input("Update employee DOB (DD/MM/YYYY): ")
            age = input("Update employee age: ")
            phone_number = input("Update employee phone number: ")

            record = ["name", "user_type", "project_name", "year_of_exp", "skill_sets", "joining_date", "DOB", "age", "phone_number"]
            temp_list = [name, user_type]

            # for project name
            if(project_name == ""):
                temp_list.append(project_name)
            else:
                temp_list.append(utility_functions.format_list(project_name))
            
            # for year of experience
            if(year_of_exp == ""):
                temp_list.append(year_of_exp)
            else:
                temp_list.append(int(year_of_exp))

            # for skill sets
            if(skill_sets == ""):
                temp_list.append(skill_sets)
            else:
                temp_list.append(utility_functions.format_list(skill_sets))

            # for joining date 
            if(joining_date == ""):
                temp_list.append(joining_date)
            else:
                temp_list.append((joining_date).replace("/", "-"))

            # for DOB 
            if(DOB == ""):
                temp_list.append(DOB)
            else:
                temp_list.append((DOB).replace("/", "-"))    

            # for age
            if(age == ""):
                temp_list.append(age)
            else:
                temp_list.append(int(age))

            # for phone number
            if(phone_number == ""):
                temp_list.append(phone_number)
            else:
                temp_list.append(int(phone_number))

            #print(temp_list)

            with open('employees_data.json', 'r') as file:
                data = json.load(file)      # json.load() takes a file object and returns the json object (key-value pair)

            for i in range(0, len(temp_list)):
                if(temp_list[i] != ""): 
                    data["emp_details"][up_employee_id_exist][record[i]] = temp_list[i]

            with open('employees_data.json', 'w') as f:
                json.dump(data, f, indent=4)

                logging.basicConfig(filename='employees_logs.txt', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
                logging.info('Employee id - {} record updated successfully'.format(up_emp_id))

                # print("Employee record updated successfully")