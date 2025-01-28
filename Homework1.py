gross_salary = input("What is your gross salary? ")
try:
    gross_salary= int(gross_salary)
    if gross_salary < 0:
        raise ValueError(f"Salaries cannot be negative")
except ValueError:
    print(f"Please introduce a valid salary")
number_children= input("How many children do you have? ")
try:
    number_children= int(number_children)
    if number_children < 0:
        print(f"Number of children cannot be negative")
except ValueError:
    print(f"Please introduce a valid number of children")

#Calculate tax based on gross salary
if gross_salary <= 1000:
    base_tax=0.1
elif 1000 < gross_salary <= 2000:
    base_tax=0.12
elif 2000 < gross_salary <= 4000:
    base_tax=0.14
else:
    base_tax=0.18
#tax cut because of the child
if gross_salary <=2000:
    tax_cut_per_child = 0.01
else:
    tax_cut_per_child = 0.005
#Total tax cut because of the child
total_tax_cut_children = number_children * tax_cut_per_child
#Total tax
total_tax= base_tax-total_tax_cut_children
#NetSalary
net_salary = gross_salary * (1 - total_tax)
print(f"your net salary is", net_salary)


