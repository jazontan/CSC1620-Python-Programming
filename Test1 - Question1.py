user_input = input("Please enter an integer (1,2,3,4 or 5): ")
#check if user input are characters and not numbers
if user_input >= 'A' and user_input <= 'z':
    print ("You have entered the wrong character, please enter the right number (1,2,3,4 or 5)")
#check if user input is not 1,2,3,4 or 5
elif int(user_input) > 5 or int(user_input)< 1:
    print ("You have entered the wrong number, please enter the right number (1,2,3,4 or 5)")
else:
    #output for input: 1
    if int(user_input) == 1:
        for x in range (1,6):
            for y in range (1,x+1):
                print ("*", end="")
            print ("")
            
    #output for input: 2
    elif int(user_input) == 2:
        for x in range (5,0,-1):
            for y in range (1, x+1):
                print ("*", end="")
            print("")

    #output for input: 3
    elif int(user_input) == 3:
        for x in range (5,0,-1):
            for y in range (5,x,-1):
                print (" ", end="")

            for y in range (1, x+1):
                print ("*", end="")
            print ("")

    #output for input: 4
    elif int (user_input) == 4:
        for x in range (1,6):
            for y in range (5,x,-1):
                print (" ", end="")

            for y in range (1,x+1):
                print ("*", end="")
            print ("")

    #output for input: 5
    else:
        #top of diamond
        for x in range (1,6):
            for y in range (5,x,-1):
                print (" ", end="")
            for y in range (1,x*2):
                print ("*", end="")
            print ("")

        #bottom of diamond
        for x in range (4,0,-1):
            for y in range (5,x,-1):
                print (" ", end="")
            for y in range (x*2,1,-1):
                print ("*", end="")
            print ("")
            
