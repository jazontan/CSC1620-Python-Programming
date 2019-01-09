#Simple Python Strings
print ("Hello World!")
print ("John replied "Hello World!"") #error is intentional for this line
print ("Then Jane yelled 'Sorry John, I only got an error'") #single quote used inside double quotes  
print("John replied \"Sorry Jane, this is the right one\"") #escape sequence for \" to print "..." within the string
print ("""Jane starts singing 'What if we rewrite the stars? 
	Say you were made to be mine' """) #triple quotes for multiline strings
print ("John sings too 'So why don’t we rewrite the stars?\nMaybe the world could be ours' ") #escape sequence for \n to move to a new line


#String Concatenation
print ("Welcome to" + "CSC1620") #"string1" + "string2" = "string1string2". Preferred concatenation method for experienced programmers
print ("Python Programming", "with lab") #"string1", "string2" = "string1 string2". Note the spacing between the 2 strings.


#String Formatting
print ("So that's all %s need to know about %s %s" % ("you", "Python", "string")) # %s acts as a placeholder for strings inside %( ... ) 
print ("So that's all %-5s need to know about %10s %s" % ("you", "Python", "string")) #-5s has trailing spaces, #10s has leading spaces 


