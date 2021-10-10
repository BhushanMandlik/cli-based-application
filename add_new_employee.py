import json     # JavaScript Object Notations
import utility_functions
import logging

class Employee:
    def __init__(self, employee_id, name, user_type, project_name, year_of_exp, skill_sets, joining_date, DOB, age, phone_number):
        self.employee_id = employee_id
        self.name = name
        self.user_type = user_type
        self.project_name = project_name
        self.year_of_exp = year_of_exp
        self.skill_sets = skill_sets
        self.joining_date = joining_date
        self.DOB = DOB
        self.age = age
        self.phone_number = phone_number

    def add_emp(self):
        if (self.user_type.lower == "admin"):
            print("User not able to add Admin")
        else:
            with open('employees_data.json', 'r') as file:
                data = json.load(file)      # json.load() takes a file object and returns the json object (key-value pair)

            exist = utility_functions.check_employee_id_exist(int(self.employee_id))    
            # print(exist)
            if(exist == 1):
                print("\nNew employee record not created because, Entered Employee id already exist! Please try with other...")
                print()
            else:
                temp_dict = {
                                "employee_id": int(self.employee_id),
                                "name": self.name,
                                "user_type": self.user_type,
                                "project_name": utility_functions.format_list(self.project_name),
                                "year_of_exp": int(self.year_of_exp),
                                "skill_sets": utility_functions.format_list(self.skill_sets),
                                "joining_date": (self.joining_date).replace("/", "-"),
                                "DOB": (self.DOB).replace("/", "-"),
                                "age": int(self.age),
                                "phone_number": int(self.phone_number)
                            }
                data["emp_details"].append(temp_dict)
                with open('employees_data.json', 'w') as f:
                    json.dump(data, f, indent=4)

                    logging.basicConfig(filename='employees_logs.txt', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
                    logging.info('New employee id - {}, name - {} record added successfully'.format(self.employee_id, self.name))
                    # print("New employee record added successfully")