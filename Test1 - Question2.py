salary = float(input("Please enter your basic salary: RM"))
increment = float(input("Please enter your annual salary increment: "))
projected_year = int(input("Please enter the number of projected years: "))
print ("YEAR\tOLD SALARY\tINCREMENT AMOUNT\tFINAL SALARY\tTAXED AMOUNT")
for year in range (1,projected_year+1):
    #start_salary = salary
    old_salary = salary
    increment_amount = salary * (increment/100)
    salary = increment_amount + salary

    if salary <= 30000 :
        taxed_amt = 0
    elif salary <= 40000:
        taxed_amt = salary * 0.03
    elif salary <= 80000:
        taxed_amt = salary * 0.06
    elif salary <= 150000:
        taxed_amt = salary * 0.1
    else:
        taxed_amt = salary * 0.15
    
    salary = salary - taxed_amt
    print ("%d\t%.2f\t%.2f\t\t%.2f\t%.2f" % (year,old_salary,increment_amount,salary,taxed_amt))
