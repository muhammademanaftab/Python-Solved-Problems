Salary=int(input('Input Basic Salary;  '))
MA=0.1*Salary
CA=0.15*Salary
HR=0.45*Salary
GS=Salary+MA+CA+HR
A=GS*12
if Salary<=200000:
    Tax=0*A
            
elif Salary<400000 and Salary>200000:
    Tax=0.1*A
       
elif Salary<600000 and Salary>400000:
    Tax=0.15*A
    
elif Salary<800000 and Salary>600000:
    Tax=0.2*A
    
else:
    Tax=0.25*A

T=Tax-GS
NS=GS-T
print (f'Output:  ')
print (f'Basic Salary:       {Salary}')
print(f'Medical Allownce:    {MA}')
print (f'Conveyance Allownce {CA}')
print(f'House Rent:          {HR}')
print('------------------------------------------------')
print (f'Gross Salary:       {GS}')
print (f'Less Tax:           {T}')
print('------------------------------------------------')
print (f'Net Salary:         {NS}')
print('------------------------------------------------')
