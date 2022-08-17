# •	Until you receive the "End" command, you will be receiving input in the format: "{companyName} -> {employeeId}".
# •	The input always will be valid.

company_employee = input()
companies_dict = {}

while not company_employee == "End":
    company = company_employee.split(" -> ")[0]
    employee = company_employee.split(" -> ")[1]
    if company not in companies_dict:
        companies_dict[company] = []
    if employee not in companies_dict[company]:
        companies_dict[company].append(employee)

    company_employee = input()

# sorted_companies_dict = sorted(companies_dict.items(), key=lambda x: x[0])
#
# for company, employees in sorted_companies_dict:
#     print(f"{company}")
#     for employee in employees:
#         print(f"-- {employee}")


for company, employees in companies_dict.items():
    print(f"{company}")
    for employee in employees:
        print(f"-- {employee}")

# # Solution 2
# company_employee = input()
# companies_dict = {}
#
# while not company_employee == "End":
#     company = company_employee.split(" -> ")[0]
#     employee = company_employee.split(" -> ")[1]
#     if company not in companies_dict:
#         companies_dict[company] = []
#     companies_dict[company].append(employee)
#     if companies_dict[company].count(employee) > 1:
#         companies_dict[company].pop()
#     company_employee = input()
#
# sorted_companies_dict = sorted(companies_dict.items())
#
# for company, employees in sorted_companies_dict:
#     print(f"{company}")
#     for employee in employees:
#         print(f"-- {employee}")
