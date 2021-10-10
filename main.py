import json     # JavaScript Object Notation
import add_new_employee
import update_employee
import delete_employee
import read_employee
import utility_functions

if __name__ == "__main__":
    print("**************************************")
    print("*                                    *")
    print("*    1. Add an employee record       *")
    print("*    2. Update an employee record    *")
    print("*    3. Delete an employee record    *")
    print("*    4. Read an employee record      *")
    print("*    5. Exit                         *")
    print("*                                    *")
    print("**************************************")

    while(1):
        print("Enter your choice (1 to 5):")
        n = input()

        try:
            asc = ord(n)

            if(asc > 48 and asc < 54):
                # Add an employee record
                if(int(n) == 1):
                    print("\n*** Add an employee record ***")
                    print()
                    print("*** Welcome ***")
                    employee_id = input("Enter employee id: ")
                    name = input("Enter employee name: ")
                    user_type = input("Enter employee user type: ")
                    project_name = input("Enter employee project name: ")
                    year_of_exp = input("Enter employee year of exp: ")
                    skill_sets = input("Enter employee skill sets: ")
                    joining_date = input("Enter employee joining date (DD/MM/YYYY): ")
                    DOB = input("Enter employee DOB (DD/MM/YYYY): ")
                    age = input("Enter employee age: ")
                    phone_number = input("Enter employee phone number: ")  

                    emp = add_new_employee.Employee(employee_id, name, user_type, project_name, year_of_exp, skill_sets, joining_date, DOB, age, phone_number)
                    emp.add_emp()
                    print()

                # Update an employee record
                elif(int(n) == 2):
                    print("\n*** Update an employee record ***")
                    update_employee.update_emp_record()
                    print()

                # Delete an employee record
                elif(int(n) == 3):
                    print("\n*** Delete an employee record ***")
                    delete_employee.delete_employee_record()
                    print()

                # Read an employee record
                elif(int(n) == 4):
                    print("\n*** All Employee's record ***\n")
                    read_employee.read_all_employee_record()
                    print()
                
                # Exit
                elif(int(n) == 5):
                    print("Thank You\n")
                    exit()

                # Invalid Input
                else:
                    print("Please enter valid input\n")
            else:
                print("Please enter valid input\n")
        except TypeError:
            print("Please enter valid input\n")