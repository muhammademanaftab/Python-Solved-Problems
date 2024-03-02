basic_salary = int (input ('Basic Salary = '))
medical_allowance = basic_salary * 0.1
conveyance_allowance = basic_salary * 0.15
house_rent = basic_salary * 0.45
gross_salary = basic_salary + medical_allowance + conveyance_allowance +house_rent
tax = gross_salary * 0.1
net_salary =  gross_salary - tax
print ('Gross Salary = ', int(gross_salary))
print ('Net Salary = ', int(net_salary))
