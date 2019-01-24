#QUESTION 1
print ("This is for Question 1")
rows = 1
while rows <= 5:
    columns = 1
    while columns <= rows:
        print ("*", end ="")
        columns += 1
    print ("")
    rows += 1

#QUESTION 2
print ("This is for Question 2")
rows = 1
while rows <= 5:
    columns = 5
    while columns > rows:       #note that there are 2 inner whiles: i) to produce the spaces
        print (" ", end="")
        columns -= 1

    columns = 1
    while columns <= rows:      #ii) to produce the stars 
        print ("*", end="")
        columns += 1

    print ("")
    rows += 1

#QUESTION 3 (a)
print ("This is for Question 3(a)")
rows = 1
while rows <= 5:            
    columns = 1
    while columns <= rows:
        print ("*", end="")
        columns += 1
    print ("")
    rows += 1

rows = 1
while rows <= 4:            #note that there are 2 outer while loop to produce the 2 sets of stars
    columns = 5
    while columns > rows:
        print ("*", end="")
        columns -= 1
    print ("")
    rows += 1

#QUESTION 3 (b)
print ("This is for Question 3 (b)")
#this 1st outer while loop will produce the top part of the pattern
rows = 1
while rows <= 5:

    #this 1st inner while loop will produce the spaces
    columns = 5
    while columns > rows:
        print (" ", end="")
        columns -= 1
    columns = 1

    #this 2nd inner while loop will produce the stars
    while columns <= rows:
        print ("*", end="")
        columns += 1
    print ("")
    rows += 1

#this 2nd outer loop will produce the bottom part of the pattern
rows = 1
while rows <= 4:

    #this 1st inner while loop will produce the spaces
    columns = 1
    while columns <= rows:
        print (" ", end="")
        columns += 1

    #this 2nd inner while loop will produce the stars
    columns = 5
    while columns > rows:
        print ("*", end="")
        columns -= 1

    print("")
    rows += 1


#QUESTION 4 (a)
print ("This is for Question 4(a)")
rows = 1
while rows <= 4:
    #this 1st inner while loop will produce the spaces required
    columns = 4
    while columns > rows:
        print (" ",end="")
        columns -= 1

    #this 2nd inner while loop will produce stars
    #calculation to produce odd stars is: (row number * 2) - 1
    columns = (rows*2)-1
    while columns >= 1:
        print ("*", end="")
        columns -=1

    print ("")
    rows += 1

#QUESTION 4 (b)
print ("This is for Question 4(b)")
rows = 1
while rows <= 4:
    #this 1st inner while loop will produce the spaces required
    columns = 4
    while columns > rows:
        print (" ",end="")
        columns -= 1

    #this 2nd inner while loop will produce stars
    #calculation to produce even stars is: row number * 2
    columns = (rows*2)
    while columns >= 1:
        print ("*", end="")
        columns -=1
        
    print ("")
    rows += 1
    
