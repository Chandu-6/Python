#Type conversions
#Created by Chandana p
#Created on 21/12/23

#int to bool
salary = 30000
isCredited = False
bSalary = bool(salary)
print("the salary is credited:", isCredited,"check:",bool(salary))
Updatedsalary = bSalary+ 1000
print(Updatedsalary)
bUpdatedsalary = bool(Updatedsalary)
print("the updated salary:",isCredited,"check",bool(Updatedsalary),"the type of updatedsalary:",type(bUpdatedsalary))
print("It is a Downcasting")

#int to float
salary=30000
bsalary=float(salary)
print("the salary is:",isCredited,"check",float(salary))
Updatedsalary=bsalary+1000
print(Updatedsalary)
print("the updated salary is:",isCredited,"check",float(Updatedsalary),"the type of updated salary is:",type(Updatedsalary))
print("It is upcasting")

#int to string
salary=20000
bsalary=str(salary)
print("the salary is:",isCredited,"check",str(salary),type(bsalary))
# Updatedsalary=bsalary+1000
# print(Updatedsalary)
# print("the updated salary is:",isCredited,"check",float(Updatedsalary),"the type of updated salary is:",type(Updatedsalary))
# print("It is upcasting")

 #Float to int
salary=3000.10
bsalary=int(salary)
print("the salary is:",int(salary))
Updatedsalary=bsalary+1000
print(Updatedsalary)
bUpdatedsalary=int(bUpdatedsalary)
print("the updated salary is:",int(Updatedsalary),"the type of updated salary is:",type(bUpdatedsalary))
print("It is Downcasting")

#Float to bool
salary=3000.1
bsalary=bool(salary)
print("the salary is:",isCredited,"check",bool(salary))
Updatedsalary=bsalary+1000
print(Updatedsalary)
bUpdatedsalary=bool(bUpdatedsalary)
print("the updated salary is:","check",bool(Updatedsalary),"the type of updated salary is:",type(bUpdatedsalary))
print("It is upcasting")


#float to string
salary=30000
bSalary = str(salary)
print("the salary is credited:",str(salary),type(bSalary))
# Updatedsalary=bSalary+1000
# print(Updatedsalary)
# bUpdatedsalary = str(Updatedsalary)
# print("the updated salary:",isCredited,"check",str(Updatedsalary),"the type of updatedsalary:",type(bUpdatedsalary))
# print("It is a Downcasting")


#String to int
salary="1000"
print(type(salary))
bSalary = int(salary)
print("the salary is credited:","check",int(salary),type(bSalary))

#String to float
salary="1000"
print(type(salary))
bSalary = float(salary)
print("the salary is credited:","check",float(salary),type(bSalary))

#String to bool
salary="1000"
print(type(salary))
bSalary = bool(salary)
print("the salary is credited:","check",bool(salary),type(bSalary))

#bool to int
salary=True
isCredited=False
bSalary = int(salary)
print("the salary is credited:",isCredited,"check:",int(salary),bool(salary))
Updatedsalary=bSalary+1000
print(Updatedsalary)
bUpdatedsalary = int(Updatedsalary)
print("the updated salary:",isCredited,"check",int(Updatedsalary),"the type of updatedsalary:",type(bUpdatedsalary))
print("It is a upcasting")

#bool to float
salary=True
bsalary=float(salary)
print("the salary is:",isCredited,"check",float(salary))
Updatedsalary=bsalary+1000
print(Updatedsalary)
bUpdatedsalary=float(bUpdatedsalary)
print("the updated salary is:","check",float(Updatedsalary),"the type of updated salary is:",type(bUpdatedsalary))
print("It is upcasting")

#bool to string
salary=True
bsalary=str(salary)
print("the salary is:",isCredited,"check",str(salary))
Updatedsalary=bsalary+1000
print(Updatedsalary)
bUpdatedsalary=str(bUpdatedsalary)
print("the updated salary is:","check",str(Updatedsalary),"the type of updated salary is:",type(bUpdatedsalary))
print("It is upcasting")









