#QUESTION 1
print ("This is for Question 1")
maxrows = int(input("Enter integer for number of stars on widest part of the pattern: "))
rows = 1
while rows <= maxrows:
    columns = 1
    while columns <= rows:
        print ("*", end="")
        columns += 1
    print ("")
    rows += 1

#QUESTION 2
print ("\n\nThis is for Question 2")
maxrows = int(input("Enter integer for number of stars on widest part of the pattern: "))
rows = 1
while rows <= maxrows:
    columns = maxrows
    while columns > rows:
        print (" ", end="")
        columns -= 1

    columns = 1
    while columns <= rows:
        print ("*", end="")
        columns += 1

    print ("")
    rows += 1

#QUESTION 3 (a)
print ("\n\nThis is for Question 3 (a)")
maxrows = int(input("Enter integer for number of stars on widest part of the pattern: "))
rows = 1
while rows <= maxrows:
    column = 1
    while column <= rows:
        print ("*", end="")
        column += 1
    print ("")
    rows += 1

rows = 1
while rows <= maxrows - 1:
    column = maxrows
    while column > rows:
        print ("*", end="")
        column -= 1
    print ("")
    rows += 1

#QUESTION 3 (b)
print ("\n\nThis is for Question 3 (b)")
maxrows = int(input("Enter integer for number of stars on widest part of the pattern: "))
rows = 1
while rows <= maxrows:
    column = maxrows
    while column > rows:
        print (" ", end="")
        column -= 1

    column = 1
    while column <= rows:
        print ("*", end="")
        column += 1

    print ("")
    rows += 1

rows = 1
while rows <= maxrows - 1:
    column = 1
    while column <= rows:
        print (" ", end="")
        column += 1

    column = maxrows
    while column > rows:
       print ("*", end="")
       column -= 1

    print ("")
    rows += 1

#QUESTION 4 (a)
print ("\n\nThis is for Question 4 (a)")
maxrows = int(input("Enter ODD integer for number of stars on widest part of the pattern: "))
maxrows = round(maxrows/2)
rows = 1
while rows <= maxrows:
    column = maxrows
    while column > rows:
        print (" ", end="")
        column -= 1

    column = (rows*2)-1
    while column >= 1:
        print ("*", end="")
        column -= 1
        
    print ("")
    rows += 1

#QUESTION 4(b)
print ("\n\nThis is for Question 4 (b)")
maxrows = int(input("Enter EVEN integer for number of stars on widest part of the pattern: "))
maxrows = round(maxrows/2)
rows = 1
while rows <= maxrows:
    column = maxrows
    while column > rows:
        print (" ", end="")
        column -= 1

    column = (rows*2)
    while column >= 1:
        print ("*", end="")
        column -= 1
        
    print ("")
    rows += 1
