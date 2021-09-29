import json     # JavaScript Object Notation

class Employee:
    # emp_list = []

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
        f = open('employee_data.json')
        data = json.load(f)     # json.load() takes a file object and returns the json object (key-value pair)

        if (self.user_type == "Admin"):
            print("User not able to add Admin")
        else:
            with open('employee_data.json', 'r+') as file:
                temp_dict = {
                                "employee_id": self.employee_id,
                                "name": self.name,
                                "user_type": self.user_type,
                                "project_name": self.project_name,
                                "year_of_exp": self.year_of_exp,
                                "skill_sets": self.skill_sets,
                                "joining_date": self.joining_date,
                                "DOB": self.DOB,
                                "age": self.age,
                                "phone_number": self.phone_number
                            }
                file_data = json.load(file)
                file_data["emp_details"].append(temp_dict)
                file.seek(0)
                json.dump(file_data, file, indent=4)
            print("New employee record added successfully")

while(1):
    print("**************************************")
    print("*                                    *")
    print("*    1. Add an employee record       *")
    print("*    2. Update an employee record    *")
    print("*    3. Delete an employee record    *")
    print("*    4. Read an employee record      *")
    print("*    5. Exit                         *")
    print("*                                    *")
    print("**************************************")

    print("Enter your choice (1 to 5):")
    n = int(input())

    # Add an employee record
    if(n == 1):
        print()
        print("*** Welcome ***")
        print("Enter employee id: ")
        employee_id = input()
        print("Enter employee name: ")
        name = input()
        print("Enter employee user type: ")
        user_type = input()
        print("Enter employee project name: ")
        project_name = input()
        print("Enter employee year of exp: ")
        year_of_exp = input()
        print("Enter employee skill sets: ")
        skill_sets = input()
        print("Enter employee joining date: ")
        joining_date = input()
        print("Enter employee DOB: ")
        DOB = input()
        print("Enter employee age: ")
        age = input()
        print("Enter employee phone number: ")
        phone_number = input()

        # -------
        emp_id_exist = 0

        f = open('employee_data.json')
        data = json.load(f)     # json.load() takes a file object and returns the json object (key-value pair)

        for i in range(0, len(data["emp_details"])):
            if(data["emp_details"][i]["user_type"] == "Admin"):
                admin_id = data["emp_details"][i]["employee_id"]
                # print(admin_id)
                break

        for i in range(0, len(data["emp_details"])):
            if(data["emp_details"][i]["employee_id"] == employee_id or employee_id == admin_id):
                emp_id_exist = 1
                f.close()
                break
        
        if(emp_id_exist == 1):
            print("Employee id already exist! Try again...")
            print()
        else:
            emp = Employee(employee_id, name, user_type, project_name, year_of_exp, skill_sets, joining_date, DOB, age, phone_number)
            emp.add_emp()
            print()
        # ------

    # Update an employee record
    elif(n == 2):
        print("*** Update an employee record ***")
        print("Enter Employee id to update record: ")
        u_e_id = input()


        f = open('employee_data.json')
        obj = json.load(f)     # json.load() takes a file object and returns the json object (key-value pair)

        ad_c = 0
        for i in range(0, len(obj["emp_details"])):
            if(obj["emp_details"][i]["employee_id"] == u_e_id):
                if(obj["emp_details"][i]["user_type"] == "Admin"):
                    ad_c = 1
                    break

        if(ad_c == 1):
            print("You can't update the Admin data")
            f.close()
            print()
        else:
            emp_c = 0

            for i in range(0, len(obj["emp_details"])):
                if(obj["emp_details"][i]["employee_id"] == u_e_id):
                    Employee.index = i
                    emp_c = 1
                    break

            if(emp_c == 0):
                print("Please enter valid employee id")
                f.close()
                print()
            else:
                # print("emp id exist")
                print("1. Update Employee Name")
                print("2. Update Employee User Type")
                print("3. Update Employee Project Name")
                print("4. Update Employee Year of Experience")
                print("5. Update Employee Skill Sets")
                print("6. Update Employee Joining Date")
                print("7. Update Employee DOB")
                print("8. Update Employee Age")
                print("9. Update Employee Phone Number")
                print("10. Exit")

                print()
                print("Enter Your Choice (1 to 10):")
                x = int(input())

                # update employee name
                if(x == 1):
                    print("Enter employee name to be updated:")
                    e_name_up = input()

                    f = open('employee_data.json')
                    obj = json.load(f)  # json.load() takes a file object and returns the json object (key-value pair)
                    # obj = json.load(open("employee_data.json"))

                    obj["emp_details"][Employee.index]["name"] = e_name_up

                    open("employee_data.json", "w").write(
                        json.dumps(obj, indent=4)
                    )

                    print("Employee name updated successfully")
                    print()
                    f.close()

                # update employee user type
                elif(x == 2):
                    print("Enter employee user type to be updated:")
                    e_user_type_up = input()

                    f = open('employee_data.json')
                    obj = json.load(f)  # json.load() takes a file object and returns the json object (key-value pair)
                    # obj = json.load(open("employee_data.json"))

                    obj["emp_details"][Employee.index]["user_type"] = e_user_type_up

                    open("employee_data.json", "w").write(
                        json.dumps(obj, indent=4)
                    )

                    print("Employee user type updated successfully")
                    print()
                    f.close()

                # update employee project name
                elif (x == 3):
                    print("Enter employee project name to be updated:")
                    e_project_name_up = input()

                    f = open('employee_data.json')
                    obj = json.load(f)  # json.load() takes a file object and returns the json object (key-value pair)
                    # obj = json.load(open("employee_data.json"))

                    obj["emp_details"][Employee.index]["project_name"] = e_project_name_up

                    open("employee_data.json", "w").write(
                        json.dumps(obj, indent=4)
                    )

                    print("Employee project name updated successfully")
                    print()
                    f.close()

                # update employee year of experience
                elif (x == 4):
                    print("Enter employee year of experience to be updated:")
                    e_year_of_exp_up = input()

                    f = open('employee_data.json')
                    obj = json.load(f)  # json.load() takes a file object and returns the json object (key-value pair)
                    # obj = json.load(open("employee_data.json"))

                    obj["emp_details"][Employee.index]["year_of_exp"] = e_year_of_exp_up

                    open("employee_data.json", "w").write(
                        json.dumps(obj, indent=4)
                    )

                    print("Employee year of experience updated successfully")
                    print()
                    f.close()

                # update employee skill set
                elif (x == 5):
                    print("Enter employee skill sets to be updated:")
                    e_skill_sets_up = input()

                    f = open('employee_data.json')
                    obj = json.load(f)  # json.load() takes a file object and returns the json object (key-value pair)
                    # obj = json.load(open("employee_data.json"))

                    obj["emp_details"][Employee.index]["skill_sets"] = e_skill_sets_up

                    open("employee_data.json", "w").write(
                        json.dumps(obj, indent=4)
                    )

                    print("Employee skill sets updated successfully")
                    print()
                    f.close()

                # update employee joining date
                elif (x == 6):
                    print("Enter employee joining date to be updated:")
                    e_joining_date_up = input()

                    f = open('employee_data.json')
                    obj = json.load(f)  # json.load() takes a file object and returns the json object (key-value pair)
                    # obj = json.load(open("employee_data.json"))

                    obj["emp_details"][Employee.index]["joining_date"] = e_joining_date_up

                    open("employee_data.json", "w").write(
                        json.dumps(obj, indent=4)
                    )

                    print("Employee joining date updated successfully")
                    print()
                    f.close()

                # update employee DOB
                elif (x == 7):
                    print("Enter employee DOB to be updated:")
                    e_dob_up = input()

                    f = open('employee_data.json')
                    obj = json.load(f)  # json.load() takes a file object and returns the json object (key-value pair)
                    # obj = json.load(open("employee_data.json"))

                    obj["emp_details"][Employee.index]["DOB"] = e_dob_up

                    open("employee_data.json", "w").write(
                        json.dumps(obj, indent=4)
                    )

                    print("Employee DOB updated successfully")
                    print()
                    f.close()

                # update employee age
                elif (x == 8):
                    print("Enter employee age to be updated:")
                    e_age_up = input()

                    f = open('employee_data.json')
                    obj = json.load(f)  # json.load() takes a file object and returns the json object (key-value pair)
                    # obj = json.load(open("employee_data.json"))

                    obj["emp_details"][Employee.index]["age"] = e_age_up

                    open("employee_data.json", "w").write(
                        json.dumps(obj, indent=4)
                    )

                    print("Employee age updated successfully")
                    print()
                    f.close()

                # update employee phone number
                elif (x == 9):
                    print("Enter employee phone number to be updated:")
                    e_phone_number_up = input()

                    f = open('employee_data.json')
                    obj = json.load(f)  # json.load() takes a file object and returns the json object (key-value pair)
                    # obj = json.load(open("employee_data.json"))

                    obj["emp_details"][Employee.index]["phone_number"] = e_phone_number_up

                    open("employee_data.json", "w").write(
                        json.dumps(obj, indent=4)       # dumps() method converts a Python object into a json string
                    )

                    print("Employee phone number updated successfully")
                    print()
                    f.close()

                # exit
                elif (x == 10):
                    print("Exited from update section")

                # invalid choice
                else:
                    print("Please enter valid choice")
                    print()
        f.close()
        print()

    # Delete an employee record
    elif(n == 3):
        print()
        print("*** Delete an employee record ***")
        print("Enter Employee id to delete record: ")
        d_e_id = input()

        f = open('employee_data.json')
        data = json.load(f)     # json.load() takes a file object and returns the json object (key-value pair)

        c = 0
        for i in range(0, len(data["emp_details"])):
            if(data["emp_details"][i]["user_type"] == "Admin" and data["emp_details"][i]["employee_id"] == d_e_id):
                c = 1
                print("Admin data not Deletable")
                print()
                break
            else:
                if data["emp_details"][i]["employee_id"] == d_e_id:
                    data["emp_details"].pop(i)
                    c = 1

                    open("employee_data.json", "w").write(
                        json.dumps(data, indent=4)       # dumps() method converts a Python object into a json string
                    )

                    print("Employee record deleted successfully")
                    #print(i)
                    f.close()
                    break

        if(c == 0):
            print("Please enter valid employee id")
            f.close()
        f.close()
        print()

    # Read an employee record
    elif(n == 4):
        print()
        print("*** Employee's record ***")
        f = open('employee_data.json')
        data = json.load(f)     # json.load() takes a file object and returns the json object (key-value pair)

        for i in range(0, len(data["emp_details"])):
            # print(i)
            if(data["emp_details"][i]["user_type"] != "Admin"):
                print(data["emp_details"][i])
            else:
                continue

        f.close()
        print()

    # Exit
    elif(n == 5):
        print("Thank You")
        print()
        break

    # Invalid Input
    else:
        print("Please enter valid input")
        print()