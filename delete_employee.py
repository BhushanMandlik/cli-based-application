import json     # JavaScript Object Notation
import utility_functions

def delete_employee_record():
    d_emp_id = input("Enter Employee id to delete record: ")

    usertype_is_admin = utility_functions.check_employee_usertype_is_admin(int(d_emp_id))

    if(usertype_is_admin == 1):
        print("Admin data not Deletable")
        print()
    else:
        employee_id_exist = utility_functions.del_check_employee_id_exist(int(d_emp_id))
        # print(employee_id_exist)

        if(employee_id_exist == 0):
            print("Employee id not exist")
        else:
            decision_to_delete_record = input("Are you sure to delete employee record (Y/N):")

            with open('employees_data.json', 'r') as file:
                data = json.load(file)      # json.load() takes a file object and returns the json object (key-value pair)

            if(decision_to_delete_record == "Y"):
                data["emp_details"].pop(employee_id_exist)

                with open('employees_data.json', 'w') as file:
                    json.dump(data, file, indent=4)       

                print("Employee record deleted successfully")
            elif(decision_to_delete_record == "N"):
                print("Sucessfully out of delete section")
            else:
                print("Please valid input")