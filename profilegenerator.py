import os

count_file = 'employee_count.txt'
if os.path.exists(count_file):
    with open(count_file, 'r') as f:
        count = int(f.read().strip())
else:
    count = 1

employee_code = f'DEV-2026-JD-{count:03d}'
department = employee_code[0:3]
print(department) 
year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code)
print(initials)
last_three = employee_code[-3:]
print(last_three)

first_name = input("Enter your First Name : ")
last_name = input("Enter Your Last Name : ")
full_name = first_name + ' ' + last_name
address = input("Enter your Residential Address : ")
employee_age = int(input("Enter your Age : "))
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = int(input("Enter your Years of Experience : "))
employee_contact = int(input("Enter your Mobile Number :"))
employee_email = input("Enter your Email ID : ")
mobile_no = "9876543210"
email = "TRmanager@gmail.com"
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

positions = {
    1: ("Junior Developer", 30000),
    2: ("Developer", 50000),
    3: ("Senior Developer", 70000),
    4: ("Manager", 90000),
    5: ("Lead", 120000)
}

print("Available Positions:")
for key, (pos, _) in positions.items():
    print(f"{key}. {pos}")

position_choice = int(input("Enter the number for your Position: "))
position, base_salary = positions[position_choice]
salary = base_salary + (experience_years * 5000)    
salary = min(salary, 150000)  

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ₹{salary} | Contact: {employee_contact} | Email: {employee_email}'
print(employee_card)
print("----FOR FURTHER HELP ----")
print("Contact : ",mobile_no)
print("Email   : ",email)
with open(count_file, 'w') as f:
    f.write(str(count + 1))