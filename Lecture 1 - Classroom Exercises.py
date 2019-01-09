#PLACEHOLDERS FOR INTEGERS (%d), FLOAT(%f) AND STRING (%s)
print ("Python treats this as integer: %d" % (4.55)) #automatic conversion from float to integer
print ("Python treats this as a floating point number: %f" % (4)) #automatic conversion from integer to float
print ("Python treats this as a string: %s" % (4.55)) #automatic conversion from float to string


#OUTPUT FOR PRACTICE 1
print ("""My name is %s and I am a %s student of %s.
I am taking %s because I want to be a %s.
I will be going to %s in %d.
My current GPA is %.2f""" % ("Callum Song", "ADTP", "MCKL", "CSC1620", "software engineer", "UC Illinois", 2020, 4.00))


#MATHEMATICAL OPERATORS IN print() FUNCTION
print("Current temperature: %.1fC\nYesterday's temperature: %.1fC\nTotal %s in temperature: %.2f %%" % (32.5, 27.8, "increase", (32.5-27.8)/ 0.325))
# %% is used to print out the '%' symbol in the string.


#FOOD PRICE EXERCISE
print ("""Discount\tFried Rice\tFried Noodles\tFried Chicken\tFried Egg
No discount\tRM %.2f\t\tRM %.2f\t\tRM %.2f\t\tRM %.2f
10%% discount\tRM %.2f\t\tRM %.2f\t\tRM %.2f\t\tRM %.2f 
25%% discount\tRM %.2f\t\tRM %.2f\t\tRM %.2f\t\tRM %.2f
50%% discount\tRM %.2f\t\tRM %.2f\t\tRM %.2f\t\tRM %.2f""" % (7,6,3.5,1.5,7*0.9, 6*0.9, 3.5*0.9, 1.5*0.9, 7*0.75, 6*0.75, 3.5*0.75, 1.5*0.75, 7*0.5, 6*0.5, 3.5*0.5, 1.5*0.5))

#ALTERNATIVE ANSWER TO FOOD PRICE EXERCISE (this code is cleaner and easier to see)
print ("Discount\tFried Rice\tFried Noodles\tFried Chicken\tFried Egg")
print ("No discount\tRM %.2f\t\tRM %.2f\t\tRM %.2f\t\tRM %.2f" % (7,6,3.5,1.5))
print ("10%% discount\tRM %.2f\t\tRM %.2f\t\tRM %.2f\t\tRM %.2f" % (7*0.9, 6*0.9, 3.5*0.9, 1.5*0.9)) 
print ("25%% discount\tRM %.2f\t\tRM %.2f\t\tRM %.2f\t\tRM %.2f" % (7*0.75, 6*0.75, 3.5*0.75, 1.5*0.75))
print ("50%% discount\tRM %.2f\t\tRM %.2f\t\tRM %.2f\t\tRM %.2f" % (7*0.5, 6*0.5, 3.5*0.5, 1.5*0.5))


#SIMPLE VARIABLES EXERCISE
course_name = "Python Programming with lab" 
student_num = 45
print ("This is %s and we have %s students" % (course_name, student_num))


#ANOTHER SIMPLE VARIABLE EXERCISE
opening_cash = 445.20
closing_cash = 812.45
sales_person = "Halen"
total_sales_today = closing_cash - opening_cash
print ("Today we earned %.2f from %s" % (total_sales_today,sales_person))
